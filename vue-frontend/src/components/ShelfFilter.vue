<template>
  <div class="shelf-filter">
    <h3>Shelves</h3>
    <ul>
      <li @click="filterShelf('all')">All</li>
      <li @click="filterShelf('read')">Read</li>
      <li @click="filterShelf('want-to-read')">Want to Read</li>
      <li @click="filterShelf('currently-reading')">Currently Reading</li>
      <li @click="filterShelf('dumped')">dumped</li>
      <!-- Add more shelves as needed -->
    </ul>
  </div>
</template>

<script>
export default {
  methods: {
    filterShelf(shelf) {
      this.$emit('filter-shelf', shelf);
    },
  },
};
</script>

<style scoped>
/* Add your styling here */
.shelf-filter {
  border: 1px solid #ccc;
  padding: 10px;
  margin: 10px;
}

.shelf-filter ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

.shelf-filter li {
  cursor: pointer;
  margin-bottom: 5px;
}
</style>
