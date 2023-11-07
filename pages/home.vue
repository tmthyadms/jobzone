<template>
  <AppHero>
    <AppCard>
      <template #body>
        <h1>{{ profile }}</h1>
      </template>
    </AppCard>
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
