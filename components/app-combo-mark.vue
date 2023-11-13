<template>
  <button
    type="button"
    id="app-combo-mark"
    class="flex items-center gap-2"
    @click="scrollToTop"
  >
    <img src="images/logo/jz-32.png" alt="" class="app-img" />
    <span class="hidden md:inline font-bold text-xl normal-case"
      >Job<span class="text-primary">zone</span></span
    >
  </button>
</template>

<script>
export default {
  methods: {
    scrollToTop() {
      window.scrollTo({ top: 0, behavior: 'auto' });
    },
  },
};
</script>
