<template>
  <svg :width="width" :height="fallbackHeight" :fill="fill"></svg>
</template>

<script>
export default {
  props: {
    width: {
      type: Number,
      default: 16,
    },
    height: {
      type: Number,
    },
    fill: {
      type: String,
      default: 'currentColor',
    },
  },
  computed: {
    fallbackHeight() {
      return this.height || this.width;
    },
  },
};
</script>
