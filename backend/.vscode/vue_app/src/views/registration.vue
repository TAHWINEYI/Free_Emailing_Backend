<template>
    <div class="registration-container">
      <h2>User Registration</h2>
      <div v-if="errorMessage" class="error-message">{{ errorMessage }}</div>
      <form @submit.prevent="submitForm">
        <label for="username">Username:</label>
        <input type="text" id="username" v-model="username" required>
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
        username: '',
        email: '',
        password: '',
        errorMessage: ''
      };
    },
    methods: {
      submitForm() {
        // Perform registration logic here
        // Make an API call to the backend to register the user
        // Example using axios:
        axios.post('/registration', {
          username: this.username,
          email: this.email,
          password: this.password
        })
        .then(response => {
          // Registration success handling
          this.username = '';
          this.email = '';
          this.password = '';
          this.$router.push('/login');
        })
        .catch(error => {
          // Registration error handling
          this.errorMessage = 'Registration failed. Please try again.';
        });
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
  