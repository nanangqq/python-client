import os
import uuid
import unittest

from indradb import *

class ClientTestCase(unittest.TestCase):
    def setUp(self):
        self.client = Client(os.environ["INDRADB_HOST"])

    def test_index_property(self):
        self.client.index_property("foo")

    def test_create_vertex(self):
        id = uuid.uuid4()
        v1 = Vertex(id, "foo")
        self.client.create_vertex(v1)
        v2 = list(self.client.get_vertices(SpecificVertexQuery(id)))
        self.assertEqual(v2, [v1])

    def test_create_vertex_from_type(self):
        id = self.client.create_vertex_from_type("foo")
        self.assertIsInstance(id, uuid.UUID)

    def test_get_vertices(self):
        id = self.client.create_vertex_from_type("foo")
        results = list(self.client.get_vertices(SpecificVertexQuery(id)))
        self.assertEqual(results, [Vertex(id, "foo")])

    def test_delete_vertices(self):
        id = self.client.create_vertex_from_type("foo")
        self.client.delete_vertices(SpecificVertexQuery(id))
        results = list(self.client.get_vertices(SpecificVertexQuery(id)))
        self.assertEqual(results, [])

    def test_get_vertex_count(self):
        results = self.client.get_vertex_count()
        self.assertGreater(results, 0)

    def test_get_edges(self):
        outbound_id = self.client.create_vertex_from_type("foo")
        inbound_id = self.client.create_vertex_from_type("foo")
        key = EdgeKey(outbound_id, "bar", inbound_id)
        self.client.create_edge(key)
        results = list(self.client.get_edges(SpecificEdgeQuery(key)))
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].key, key)

    def test_delete_edges(self):
        outbound_id = self.client.create_vertex_from_type("foo")
        inbound_id = self.client.create_vertex_from_type("foo")
        key = EdgeKey(outbound_id, "bar", inbound_id)
        self.client.create_edge(key)
        self.client.delete_edges(SpecificEdgeQuery(key))
        count = self.client.get_edge_count(outbound_id, None, EdgeDirection.OUTBOUND)
        self.assertEqual(count, 0)

    def test_get_edge_count(self):
        outbound_id = self.client.create_vertex_from_type("foo")
        inbound_id = self.client.create_vertex_from_type("foo")
        key = EdgeKey(outbound_id, "bar", inbound_id)
        self.client.create_edge(key)
        count = self.client.get_edge_count(outbound_id, None, EdgeDirection.OUTBOUND)
        self.assertEqual(count, 1)

    def test_vertex_properties(self):
        id = self.client.create_vertex_from_type("foo")
        query = SpecificVertexQuery(id).property("foo")

        m1 = list(self.client.get_vertex_properties(query))
        self.client.set_vertex_properties(query, 42)
        m2 = list(self.client.get_vertex_properties(query))
        self.client.delete_vertex_properties(query)
        m3 = list(self.client.get_vertex_properties(query))

        self.assertEqual(m1, [])
        self.assertEqual(m2, [VertexProperty(id, 42)])
        self.assertEqual(m3, [])

    def test_edge_properties(self):
        outbound_id = self.client.create_vertex_from_type("foo")
        inbound_id = self.client.create_vertex_from_type("foo")
        key = EdgeKey(outbound_id, "bar", inbound_id)
        self.client.create_edge(key)
        query = SpecificEdgeQuery(key).property("foo")

        m1 = list(self.client.get_edge_properties(query))
        self.client.set_edge_properties(query, 42)
        m2 = list(self.client.get_edge_properties(query))
        self.client.delete_edge_properties(query)
        m3 = list(self.client.get_edge_properties(query))

        self.assertEqual(m1, [])
        self.assertEqual(m2, [EdgeProperty(key, 42)])
        self.assertEqual(m3, [])

    def test_get_all_vertex_properties(self):
        id = self.client.create_vertex_from_type("foo")
        query = SpecificVertexQuery(id)

        m1 = list(self.client.get_all_vertex_properties(query))
        self.client.set_vertex_properties(query.property("foo"), 42)
        m2 = list(self.client.get_all_vertex_properties(query))
        self.client.delete_vertex_properties(query.property("foo"))
        m3 = list(self.client.get_all_vertex_properties(query))

        self.assertEqual(m1, [VertexProperties(Vertex(id, "foo"), [])])
        self.assertEqual(m2, [VertexProperties(Vertex(id, "foo"), [NamedProperty("foo", 42)])])
        self.assertEqual(m3, [VertexProperties(Vertex(id, "foo"), [])])

    def test_get_all_edge_properties(self):
        outbound_id = self.client.create_vertex_from_type("foo")
        inbound_id = self.client.create_vertex_from_type("foo")
        key = EdgeKey(outbound_id, "bar", inbound_id)
        self.client.create_edge(key)
        query = SpecificEdgeQuery(key)

        m1 = list(self.client.get_all_edge_properties(query))
        self.client.set_edge_properties(query.property("foo"), 42)
        m2 = list(self.client.get_all_edge_properties(query))
        self.client.delete_edge_properties(query.property("foo"))
        m3 = list(self.client.get_all_edge_properties(query))

        self.assertEqual(len(m1), 1)
        self.assertEqual(m1[0].edge.key, key)
        self.assertEqual(m1[0].props, [])

        self.assertEqual(len(m2), 1)
        self.assertEqual(m2[0].edge.key, key)
        self.assertEqual(m2[0].props, [NamedProperty("foo", 42)])
        
        self.assertEqual(len(m3), 1)
        self.assertEqual(m3[0].edge.key, key)
        self.assertEqual(m3[0].props, [])

class BulkInserterTestCase(unittest.TestCase):
    def test_bulk_insert(self):
        client = Client(os.environ["INDRADB_HOST"])

        v1 = Vertex(uuid.uuid1(), "foo")
        v2 = Vertex(uuid.uuid1(), "foo")
        key = EdgeKey(v1.id, "bar", v2.id)

        # insert everything
        inserter = BulkInserter()
        inserter.vertex(v1)
        inserter.vertex(v2)
        inserter.edge(key)
        inserter.vertex_property(v1.id, "baz", True)
        inserter.edge_property(key, "bez", False)
        inserter.execute(client)

        # ensure vertices exist
        results = list(client.get_vertices(SpecificVertexQuery(v1.id)))
        self.assertEqual(results, [v1])
        results = list(client.get_vertices(SpecificVertexQuery(v2.id)))
        self.assertEqual(results, [v2])

        # ensure the edge exists
        results = list(client.get_edges(SpecificEdgeQuery(key)))
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].key, key)

        # ensure the vertex property exists
        query = SpecificVertexQuery(v1.id).property("baz")
        results = list(client.get_vertex_properties(query))
        self.assertEqual(results, [VertexProperty(v1.id, True)])

        # ensure the edge property exists
        query = SpecificEdgeQuery(key).property("bez")
        results = list(client.get_edge_properties(query))
        self.assertEqual(results, [EdgeProperty(key, False)])
