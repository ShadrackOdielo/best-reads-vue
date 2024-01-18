<template>
  <div class="book-card" @mouseover="showDetails" @mouseout="hideDetails">
    <img :src="book.image" alt="Book Cover" @click="redirectToDetailsPage" />
    <div class="details" v-show="detailsVisible">
      <h3>{{ book.title }}</h3>
      <p>{{ book.author }}</p>
      <!-- Additional details, e.g., ratings and synopsis -->
      <div v-if="isAuthenticated">
        <button @click="addToShelf">Add to Shelf</button>
        <div v-show="showDropdown">
          <select v-model="selectedShelf">
            <option v-for="shelf in shelves" :key="shelf.id" :value="shelf.id">{{ shelf.name }}</option>
          </select>
          <button @click="addToSelectedShelf">Add to Selected Shelf</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    book: Object,
    isAuthenticated: Boolean,
    shelves: Array,
  },
  data() {
    return {
      detailsVisible: false,
      selectedShelf: null,
      showDropdown: false,
    };
  },
  methods: {
    showDetails() {
      this.detailsVisible = true;
    },
    hideDetails() {
      this.detailsVisible = false;
      this.showDropdown = false;
    },
    redirectToDetailsPage() {
      // For simplicity, open a new tab to simulate redirect
      window.open('https://www.example.com/book/' + this.book.id, '_blank');
    },
    addToShelf() {
      this.showDropdown = !this.showDropdown;
    },
    addToSelectedShelf() {
      // Implement adding the book to the selected shelf
      // You can use an event bus or a state management solution to handle this
      this.showDropdown = false;
    },
  },
};
</script>

<style scoped>
/* Add your styling here */
.book-card {
  position: relative;
  border: 1px solid #ccc;
  margin: 10px;
  text-align: center;
  overflow: hidden;
}

.book-card img {
  max-width: 100%;
  height: auto;
}

.details {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(255, 255, 255, 0.8);
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  opacity: 0;
  transition: opacity 0.3s;
}

.book-card:hover .details {
  opacity: 1;
}

.details h3 {
  margin: 0;
}

.details p {
  margin: 5px 0;
}

/* Add more styling as needed */
</style>
