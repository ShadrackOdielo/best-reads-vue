<template>
  <div id="home-page">
    <Section title="Top This Week from NYT Books API" :books="topBooks" :isAuthenticated="isAuthenticated" :shelves="shelves" />
    <Section title="Latest from Goodreads" :books="latestBooks" :isAuthenticated="isAuthenticated" :shelves="shelves" />
    <Section title="Classics Featuring Classic Books" :books="classics" :isAuthenticated="isAuthenticated" :shelves="shelves" />
  </div>
</template>

<script>
import Section from './Section.vue';

export default {
  components: {
    Section,
  },
  data() {
    return {
      topBooks: [
        { id: 1, title: 'Top Book 1', author: 'Author 1', image: 'https://via.placeholder.com/150' },
        { id: 2, title: 'Top Book 2', author: 'Author 2', image: 'https://via.placeholder.com/150' },
        // Add more top books as needed
      ],
      latestBooks: [
        { id: 3, title: 'Latest Book 1', author: 'Author 3', image: 'https://via.placeholder.com/150' },
        { id: 4, title: 'Latest Book 2', author: 'Author 4', image: 'https://via.placeholder.com/150' },
        // Add more latest books as needed
      ],
      classics: [
        { id: 5, title: 'Classic Book 1', author: 'Author 5', image: 'https://via.placeholder.com/150' },
        { id: 6, title: 'Classic Book 2', author: 'Author 6', image: 'https://via.placeholder.com/150' },
        // Add more classic books as needed
      ],
      isAuthenticated: true, // Replace with actual authentication status
      shelves: [
        { id: 1, name: 'Want to Read' },
        { id: 2, name: 'Currently Reading' },
        // Add more shelves as needed
      ],
    };
  },
};
</script>

<style>
/* Add your styling here */
#home-page {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
