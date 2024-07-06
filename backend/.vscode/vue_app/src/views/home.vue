<template>
  <div>
    <div class="toolbar">
      <button @click="showInbox">Inbox</button>
      <button @click="showSent">Sent</button>
      <button @click="showCompose">Compose</button>
      <button @click="showImportant">Important</button>
      <button @click="showSpam">Spam</button>
      <button @click="showOutbox">Outbox</button>
    </div>
    <div class="emails">
      <div v-if="currentTab === 'inbox'" class="email-list">
        <h2>Inbox</h2>
        <ul>
          <li v-for="email in inboxEmails" :key="email.id" @click="showEmail(email)">
            {{ email.subject }}
          </li>
        </ul>
      </div>
      <div v-if="currentTab === 'sent'" class="email-list">
        <h2>Sent</h2>
        <ul>
          <li v-for="email in sentEmails" :key="email.id" @click="showEmail(email)">
            {{ email.subject }}
          </li>
        </ul>
      </div>
      <div v-if="currentTab === 'compose'" class="compose-email">
        <h2>Compose Email</h2>
        <form @submit="sendEmail">
          <input type="text" v-model="recipient" placeholder="Recipient" required>
          <input type="text" v-model="subject" placeholder="Subject" required>
          <textarea v-model="body" placeholder="Email Body" required></textarea>
          <button type="submit">Send</button>
        </form>
      </div>
      <div v-if="currentTab === 'important'" class="email-list">
        <h2>Important</h2>
        <ul>
          <li v-for="email in importantEmails" :key="email.id" @click="showEmail(email)">
            {{ email.subject }}
          </li>
        </ul>
      </div>
      <div v-if="currentTab === 'spam'" class="email-list">
        <h2>Spam</h2>
        <ul>
          <li v-for="email in spamEmails" :key="email.id" @click="showEmail(email)">
            {{ email.subject }}
          </li>
        </ul>
      </div>
      <div v-if="currentTab === 'outbox'" class="email-list">
        <h2>Outbox</h2>
        <ul>
          <li v-for="email in outboxEmails" :key="email.id" @click="showEmail(email)">
            {{ email.subject }}
          </li>
        </ul>
      </div>
      <div v-if="currentEmail" class="email-details">
        <h2>{{ currentEmail.subject }}</h2>
        <p>{{ currentEmail.body }}</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      currentTab: 'inbox',
      inboxEmails: [
        { id: 1, subject: 'Example Email 1', body: 'This is the body of email 1.' },
        { id: 2, subject: 'Example Email 2', body: 'This is the body of email 2.' },
        { id: 3, subject: 'Example Email 3', body: 'This is the body of email 3.' }
      ],
      sentEmails: [
        { id: 4, subject: 'Example Email 4', body: 'This is the body of email 4.' },
        { id: 5, subject: 'Example Email 5', body: 'This is the body of email 5.' },
        { id: 6, subject: 'Example Email 6', body: 'This is the body of email 6.' }
      ],
      importantEmails: [
        { id: 10, subject: 'Important Email 1', body: 'This is an important email.' },
        { id: 11, subject: 'Important Email 2', body: 'This is another important email.' }
      ],
      spamEmails: [
        { id: 12, subject: 'Spam Email 1', body: 'This is a spam email.' },
        { id: 13, subject: 'Spam Email 2', body: 'This is another spam email.' }
      ],
      outboxEmails: [
        { id: 7, subject: 'Example Email 7', body: 'This is the body of email 7.' },
        { id: 8, subject: 'Example Email 8', body: 'This is the body of email 8.' },
        { id: 9, subject: 'Example Email 9', body: 'This is the body of email 9.' }
      ],
      currentEmail: null,
      recipient: '',
      subject: '',
      body: ''
    };
  },
  methods: {
    showInbox() {
      this.currentTab = 'inbox';
      this.currentEmail = null;
    },
    showSent() {
      this.currentTab = 'sent';
      this.currentEmail = null;
    },
    showCompose() {
      this.currentTab = 'compose';
      this.currentEmail = null;
    },
    showImportant() {
      this.currentTab = 'important';
      this.currentEmail = null;
    },
    showSpam() {
      this.currentTab = 'spam';
      this.currentEmail = null;
    },
    showOutbox() {
      this.currentTab = 'outbox';
      this.currentEmail = null;
    },
    showEmail(email) {
      this.currentEmail = email;
    },
    sendEmail(event) {
      event.preventDefault();
      const newEmail = {
        id: Date.now(),
        subject: this.subject,
        body: this.body
      };
      this.sentEmails.push(newEmail);
      this.currentTab = 'sent';
      this.currentEmail = newEmail;
      this.recipient = '';
      this.subject = '';
      this.body = '';
    }
  }
};
</script>

<style scoped>
.toolbar {
  margin-bottom: 20px;
}

.email-list {
  margin-bottom: 20px;
}

.email-details {
  border: 1px solid #ccc;
  padding: 10px;
}

.compose-email form {
  display: flex;
  flex-direction: column;
}

.compose-email input,
.compose-email textarea {
  margin-bottom: 10px;
}
</style>
