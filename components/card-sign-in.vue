<template>
  <AppCard class="!max-w-none !max-h-none">
    <template #body>
      <AppComboMark class="justify-center lg:justify-start mb-6" />
      <h2
        class="mb-6 font-light text-2xl lg:text-4xl text-center lg:text-start"
      >
        Sign in to unlock <br class="hidden lg:inline" />
        your <br class="inline lg:hidden" />secure future
      </h2>
      <form class="grid grid-cols-1 gap-6" @submit.prevent="signIn">
        <AppInput
          label="email"
          type="email"
          input-id="email"
          :req="true"
          ac="email"
          @input="(value) => (form.email = value)"
        />
        <InputPassword @input="(value) => (form.password = value)" />
        <button
          type="submit"
          name="sign-in"
          class="btn btn-block btn-primary"
          :disabled="isFormSubmitted"
        >
          <span v-if="isFormSubmitted" class="loading loading-infinity"></span>
          <span v-else>sign in</span>
        </button>
      </form>
      <NuxtLink
        to="/sign-up"
        class="btn btn-outline btn-primary"
        @click="$emit('flip')"
      >
        new to jobzone? join now</NuxtLink
      >
    </template>
  </AppCard>
</template>

<script>
import { mapActions } from 'vuex';

export default {
  events: ['flip'],
  data() {
    return {
      form: {
        email: '',
        password: '',
      },
      isFormSubmitted: false,
    };
  },
  methods: {
    ...mapActions('profile', ['fetchProfile']),
    async signIn() {
      try {
        this.isFormSubmitted = true;
        const response = await this.$axios.$post('/login', this.form, {
          headers: { 'Content-Type': 'application/json' },
        });
        if (!response) {
          this.isFormSubmitted = false;
          return;
        }
        await this.fetchProfile(response);
        window.scrollTo({ top: 0, behavior: 'auto' });
        this.isFormSubmitted = false;
        this.$router.push('/home');
      } catch (error) {
        console.error(error);
      }
    },
  },
};
</script>
