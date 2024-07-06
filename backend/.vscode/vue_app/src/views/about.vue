<template>
  <div>
    <Header />
    <h2>About Us</h2>
    <p>Content of the about page goes here...</p>
    <Footer />
  </div>
</template>

<script>
import Header from '@/components/Header.vue';
import Footer from '@/components/Footer.vue';

export default {
  name: 'About',
  components: {
    Header,
    Footer,
  },
};
</script>

<style scoped>
/* Add your about page styles here */
</style>