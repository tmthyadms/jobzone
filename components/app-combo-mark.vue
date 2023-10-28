<template>
  <component
    :is="componentType"
    id="app-combo-mark"
    class="flex items-center gap-2"
  >
    <img src="images/logo/jz-32.png" alt="" class="app-img" />
    <span href="#" class="font-bold text-xl normal-case"
      >Job<span class="text-primary">zone</span></span
    >
  </component>
</template>

<script>
export default {
  props: {
    link: {
      type: Boolean,
    },
  },
  computed: {
    componentType() {
      return this.link ? 'a' : 'div';
    },
  },
  mounted() {
    if (this.link)
      document.getElementById('app-combo-mark').setAttribute('href', '#');
  },
};
</script>
