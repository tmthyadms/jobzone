<template>
  <div
    class="card lg:card-side max-w-lg lg:max-h-64 bg-base-100 text-base-content shadow"
    :class="{ 'image-full': overlay, hover: hover }"
  >
    <figure v-if="figure">
      <img :src="figure" :alt="title" class="app-img object-top" />
    </figure>
    <div class="card-body">
      <slot name="body">
        <h2 v-if="title" class="card-title capitalize">
          {{ title }}
          <div v-if="badge" class="badge badge-secondary">{{ badge }}</div>
        </h2>
        <p v-if="desc" class="text-xs opacity-60">{{ desc }}</p>
        <div v-if="slot || badges" class="card-actions justify-end">
          <slot></slot>
          <div
            v-if="!slot && badges"
            v-for="badge in badges"
            class="badge badge-outline"
          >
            {{ badge }}
          </div>
        </div>
      </slot>
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
    },
    desc: {
      type: String,
    },
    badge: {
      type: String,
    },
    badges: {
      type: Array,
    },
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
