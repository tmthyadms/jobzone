<template>
  <AppHero :title="profile.fullName">
    <div class="animated fadeInUp flex-1 w-full lg:w-96"></div>
  </AppHero>
</template>

<script>
import { mapGetters } from 'vuex';

export default {
  computed: {
    ...mapGetters('profile', ['profile']),
  },
};
</script>
