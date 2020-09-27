import java.util.ArrayList;
import java.util.LinkedList;

public class HashTable<K, V> {
    private int capacity = 100;
    private int size = 0;
    private ArrayList<LinkedList<KeyValuePair>> data;

    HashTable() {
        this.data = new ArrayList<>(capacity);
        for (int i = 0; i < capacity; i++) {
            this.data.add(i, null);
        }
    }

    V put(K key, V value) {
        int index = computeIndex(key);
        LinkedList<KeyValuePair> kVPairs = getAtIndex(index);
        boolean found = false;
        for (KeyValuePair kVPair : kVPairs) {
            if (kVPair.key.equals(key)) {
                kVPair.value = value;
                found = true;
            }
        }
        if (!found) {
            kVPairs.add(new KeyValuePair(key, value));
            this.size += 1;
        }
        return value;
    }

    V get(K key) {
        int index = computeIndex(key);
        LinkedList<KeyValuePair> kVPairs = getAtIndex(index);
        for (KeyValuePair kVPair : kVPairs) {
            if (kVPair.key.equals(key))
                return kVPair.value;
        }
        return null;
    }

    V remove(K key) {
        int index = computeIndex(key);
        LinkedList<KeyValuePair> kVPairs = getAtIndex(index);
        for (int i = 0; i < kVPairs.size(); i++) {
            KeyValuePair kVPair = kVPairs.get(i);
            if (kVPair.key.equals(key)) {
                kVPairs.remove(i);
                this.size -= 1;
                return kVPair.value;
            }
        }
        return null;
    }

    int size() {
        return this.size;
    }

    private int computeIndex(K key) {
        return key.hashCode() % capacity;
    }

    private LinkedList<KeyValuePair> getAtIndex(int index) {
        LinkedList<KeyValuePair> kVPairs = data.get(index);
        if (kVPairs == null)
            data.add(index, new LinkedList<>());
        return data.get(index);
    }

    private class KeyValuePair {
        K key;
        V value;

        KeyValuePair(K key, V value) {
            this.key = key;
            this.value = value;
        }
    }
}
