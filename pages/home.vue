<template>
  <AppHero>
    <AppCard>
      <template #body>
        <h1>User _id: {{ id }}</h1>
      </template>
    </AppCard>
  </AppHero>
</template>

<script>
export default {
  data() {
    return {
      id: '',
    };
  },
  async fetch() {
    const data = await this.$axios.$post('/auths');
    this.id = data[0]._id;
    console.log(this.id);
  },
};
</script>
