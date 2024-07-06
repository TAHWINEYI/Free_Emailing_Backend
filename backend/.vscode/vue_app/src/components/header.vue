<template>
  <header>
    <div class="header-content">
      <h1>My App</h1>
      <div class="search-bar">
        <input type="text" v-model="searchQuery" placeholder="Search..." />
        <button @click="search">Search</button>
      </div>
    </div>
  </header>
</template>

<script>
export default {
  name: 'Header',
  data() {
    return {
      searchQuery: '',
    };
  },
  methods: {
    search() {
      // Perform search functionality
      // You can access the searchQuery value using 'this.searchQuery'
      console.log('Searching for:', this.searchQuery);
    },
  },
};
</script>

<style scoped>
.header-content {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px;
}

.search-bar {
  display: flex;
  align-items: center;
}

.search-bar input {
  margin-right: 10px;
}

/* Add your header styles here */
</style>