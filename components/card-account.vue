<template>
  <AppCard class="bg-base-200 app-shadow-b">
    <template #body>
      <form
        id="form-update-acc"
        class="grid grid-cols-1 gap-6"
        @submit.prevent="updateAcc"
      >
        <h2
          class="mb-6 font-light text-2xl lg:text-4xl text-center lg:text-start"
        >
          Account settings
        </h2>
        <AppInput
          label="email"
          type="email"
          :prompt="profile.email"
          input-id="email"
          :disabled="!isEditing"
          ac="email"
          @input="(value) => (form.email = value)"
        />
        <div class="space-y-2">
          <button
            type="button"
            class="btn btn-block btn-primary"
            :class="{ 'btn-outline': isEditing && !isFormSubmitted }"
            :disabled="isFormSubmitted"
            @click="isEditing = !isEditing"
          >
            {{ isEditing ? 'cancel editing' : 'edit account' }}
          </button>
          <button
            v-if="isEditing"
            type="submit"
            name="sign-up"
            class="btn btn-block btn-primary"
            :disabled="isFormSubmitted"
          >
            <span
              v-if="isFormSubmitted"
              class="loading loading-infinity"
            ></span>
            <span v-else>update account</span>
          </button>
        </div>
      </form>
    </template>
  </AppCard>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';

export default {
  data() {
    return {
      form: {
        authId: '',
        email: '',
      },
      isFormSubmitted: false,
      isEditing: false,
    };
  },
  computed: {
    ...mapGetters('profile', ['profile']),
  },
  watch: {
    isEditing(newValue) {
      // reset form when editing is cancelled
      // due to not using v-model, we need to reset the form manually
      if (!newValue) {
        document.getElementById('form-update-acc').reset();
        this.form.email = '';
      }
    },
  },
  methods: {
    ...mapActions('profile', ['updateAuth']),
    async updateAcc() {
      try {
        this.form.authId = this.profile.id;
        this.isFormSubmitted = true;
        await this.updateAuth(this.form);
        this.isFormSubmitted = false;
        this.isEditing = false;
        this.$toast.success('Account updated successfully.');
      } catch (error) {
        this.isFormSubmitted = false;
        this.$toast.error(error.message);
      }
    },
  },
};
</script>
