<template>
  <div
    class="card lg:card-side bg-base-100 text-base-content shadow"
    :class="{ 'image-full': overlay, hover: hover }"
    @click="$emit('click', $event)"
  >
    <figure v-if="figure">
      <img :src="figure" :alt="title" class="app-img object-top" />
    </figure>
    <div class="card-body">
      <slot name="body">
        <h2 v-if="title" class="card-title capitalize">
          {{ title }}
          <div v-if="titleBadge" class="badge badge-secondary">{{ badge }}</div>
        </h2>
        <h3
          v-if="subtitle"
          class="card-subtitle capitalize"
          v-html="subtitle"
        ></h3>
        <div>
          <div
            v-if="subtitleBadges"
            v-for="subtitleBadge in subtitleBadges"
            class="badge badge badge-primary capitalize"
          >
            {{ subtitleBadge }}
          </div>
        </div>
        <p v-if="desc" class="text-xs opacity-60">{{ desc }}</p>
        <slot></slot>
        <div
          v-if="!!$slots.action || badges"
          class="card-actions"
          :class="{ 'justify-end': badges }"
        >
          <slot name="action">
            <div
              v-if="badges"
              v-for="badge in badges"
              class="badge badge-outline"
            >
              {{ badge }}
            </div>
          </slot>
        </div>
      </slot>
    </div>
  </div>
</template>

<script>
export default {
  emits: ['click'],
  props: {
    title: {
      type: String,
    },
    subtitle: {
      type: String,
    },
    desc: {
      type: String,
    },
    titleBadge: {
      type: String,
    },
    subtitleBadges: {
      type: Array,
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
};
</script>

<style scoped>
.card-subtitle {
  @apply text-sm;
}

.hover {
  @apply transition transition-transform duration-300 ease-out hover:-translate-y-1;
}
</style>
