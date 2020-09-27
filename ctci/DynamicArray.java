class DynamicArray {
    int[] array;
    int size;

    DynamicArray() {
        this(1);
    }

    DynamicArray(int initialCapacity) {
        this.array = new int[initialCapacity];
        this.size = 0;
    }

    void push(int data) {
        if (this.size == this.array.length)
            this.increaseCapacity();
        this.array[this.size] = data;
        this.size += 1;
    }

    void push(int data, int index) {
        this.checkIndexInBounds(index);
        this.array[index] = data;
    }

    int get(int index) {
        this.checkIndexInBounds(index);
        return this.array[index];
    }

    void pop() {
        this.size -= 1;
    }

    public int size() {
        return this.size;
    }

    private void checkIndexInBounds(int index) {
        if (index >= this.size)
            throw new ArrayIndexOutOfBoundsException();
    }

    private void increaseCapacity() {
        int[] newArray = new int[this.array.length * 2];
        for (int i = 0; i < this.array.length; i++)
            newArray[i] = this.array[i];
        this.array = newArray;
    }
}