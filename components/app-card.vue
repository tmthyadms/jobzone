<template>
  <div
    class="card lg:card-side max-w-lg lg:max-h-64 bg-base-100 text-base-content shadow-xl"
    :class="{ 'image-full': overlay, hover: hover }"
  >
    <figure v-if="figure">
      <img :src="figure" :alt="title" class="object-top" />
    </figure>
    <div class="card-body">
      <h2 class="card-title capitalize">
        {{ title }}
        <div v-if="badge" class="badge badge-secondary">{{ badge }}</div>
      </h2>
      <p class="text-xs opacity-60">{{ desc }}</p>
      <div class="card-actions justify-end">
        <slot></slot>
        <div
          v-if="!slot && badges"
          v-for="badge in badges"
          class="badge badge-outline"
        >
          {{ badge }}
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      slot: false,
    };
  },
  props: {
    title: {
      type: String,
      required: true,
    },
    desc: {
      type: String,
    },
    badge: {
      type: String,
    },
    badges: {},
    figure: {
      type: String,
    },
    overlay: {
      type: Boolean,
    },
    hover: {
      type: Boolean,
    },
  },
  created() {
    this.slot = !!this.$slots.default;
  },
};
</script>

<style scoped>
.hover {
  @apply transition transition-transform duration-300 ease-out hover:-translate-y-1;
}
</style>
