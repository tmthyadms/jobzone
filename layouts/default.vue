<template>
  <div class="app-layout">
    <TheHeader :hasSignedIn="true" />
    <main>
      <Nuxt />
    </main>
    <TheFooter />
  </div>
</template>

<script>
export default {
  middleware: 'auth',
};
</script>
