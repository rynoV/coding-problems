import static org.junit.Assert.*;

import org.junit.Test;

public class DynamicArrayTest {
    @Test
    public void testPush() {
        DynamicArray da = new DynamicArray(2);
        da.push(1);
        assertEquals(1, da.size());
        assertEquals(1, da.get(0));
        da.push(2);
        assertEquals(2, da.size());
        assertEquals(2, da.get(1));
    }

    @Test
    public void testPushIndex() {
        DynamicArray da = new DynamicArray(2);
        da.push(1);
        da.push(2);

        da.push(4, 1);
        assertEquals(4, da.get(1));
    }

    @Test
    public void testResize() {
        DynamicArray da = new DynamicArray(1);
        da.push(1);
        da.push(2);
        assertEquals(2, da.size());
        da.push(3);
        da.push(4);
        assertEquals(4, da.size());
        da.push(5);
        da.push(6);
        assertEquals(6, da.size());
        for (int i = 0; i <= 5; i++) {
            assertEquals(i + 1, da.get(i));
        }
    }

    @Test
    public void testPop() {
        DynamicArray da = new DynamicArray(1);
        da.push(1);
        da.push(2);

        da.pop();
        assertEquals(1, da.size());
        assertEquals(1, da.get(0));
        assertThrows(ArrayIndexOutOfBoundsException.class, () -> da.get(1));
        assertThrows(ArrayIndexOutOfBoundsException.class, () -> da.push(1, 1));
        da.push(2);
        assertEquals(2, da.size());
        assertEquals(2, da.get(1));
    }
}