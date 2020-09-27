import static org.junit.Assert.*;

import org.junit.Test;

public class HashTableTest {
    @Test
    public void testPut() {
        HashTable<String, Integer> ht = new HashTable<>();
        String key = "hello";
        ht.put(key, 2);
        assertEquals((Integer) 2, ht.get(key));
        assertEquals(1, ht.size());
    }

    @Test
    public void testReplace() {
        HashTable<String, Integer> ht = new HashTable<>();
        String key = "hello";
        ht.put(key, 2);
        ht.put(key, 3);
        assertEquals((Integer) 3, ht.get(key));
        assertEquals(1, ht.size());
    }

    @Test
    public void testRemove() {
        HashTable<String, Integer> ht = new HashTable<>();
        ht.put("key1", 2);
        ht.put("key2", 3);
        assertEquals(2, ht.size());
        assertEquals((Integer) 2, ht.remove("key1"));
        assertEquals(1, ht.size());
        assertEquals(null, ht.get("key1"));
    }
}