<template>
  <svg
    xmlns="http://www.w3.org/2000/svg"
    :width="width"
    :height="fallbackHeight"
    :fill="fill"
    class="bi bi-plus"
    viewBox="0 0 16 16"
  >
    <path
      d="M8 4a.5.5 0 0 1 .5.5v3h3a.5.5 0 0 1 0 1h-3v3a.5.5 0 0 1-1 0v-3h-3a.5.5 0 0 1 0-1h3v-3A.5.5 0 0 1 8 4z"
    />
  </svg>
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
