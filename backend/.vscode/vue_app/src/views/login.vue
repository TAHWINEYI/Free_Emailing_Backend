<template>
    <div class="registration-container">
      <h2>User Registration</h2>
      <div v-if="errorMessage" class="error-message">{{ errorMessage }}</div>
      <form @submit="submitForm">
        <label for="name">Name:</label>
        <input type="text" id="name" v-model="name" required>
        <label for="email">Email:</label>
        <input type="email" id="email" v-model="email" required>
        <label for="password">Password:</label>
        <input type="password" id="password" v-model="password" required>
        <button type="submit">Register</button>
      </form>
      <div class="login-link">
        Already have an account? <router-link to="/login">Login</router-link>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        name: '',
        email: '',
        password: '',
        errorMessage: ''
      };
    },
    methods: {
      submitForm(event) {
        event.preventDefault();
        // Perform registration logic here
        // Here, you can make an API call to register the user
        // Example code to simulate registration success:
        setTimeout(() => {
          this.name = '';
          this.email = '';
          this.password = '';
          this.$router.push('/login');
        }, 1000);
      }
    }
  };
  </script>
  
  <style scoped>
  .registration-container {
    max-width: 400px;
    margin: 0 auto;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 4px;
  }
  
  .error-message {
    color: red;
    margin-bottom: 10px;
  }
  
  form {
    display: flex;
    flex-direction: column;
    margin-bottom: 10px;
  }
  
  label {
    margin-bottom: 5px;
  }
  
  input {
    padding: 5px;
    margin-bottom: 10px;
  }
  
  button {
    padding: 8px 12px;
    background-color: #007bff;
    color: #fff;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }
  
  .login-link {
    text-align: center;
  }
  </style>
  