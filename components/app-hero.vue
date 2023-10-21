<template>
  <div class="hero min-h-screen" :style="bgImg">
    <div v-if="img" class="hero-overlay bg-opacity-60"></div>
    <div
      class="hero-content"
      :class="{
        'text-neutral-content': img,
        'text-center': center,
        'flex-col lg:flex-row-reverse': !center,
      }"
    >
      <img
        v-if="!center && figure"
        :src="figure"
        alt=""
        class="max-w-sm rounded-box shadow-2xl"
      />
      <div>
        <div class="mx-auto max-w-md">
          <h1 class="text-5xl font-bold capitalize">{{ title }}</h1>
          <p v-if="desc" class="mt-5 md:text-lg xl:text-2xl opacity-60">
            {{ desc }}
          </p>
        </div>
        <div class="slot">
          <slot></slot>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    title: {
      type: String,
      required: true,
    },
    desc: {
      type: String,
    },
    img: {
      type: String,
    },
    center: {
      type: Boolean,
      default: true,
    },
    figure: {
      type: String,
    },
  },
  computed: {
    bgImg() {
      return this.img ? { backgroundImage: `url(${this.img})` } : {};
    },
  },
};
</script>

<style scoped>
.slot {
  @apply mt-5;
}

.slot:empty {
  @apply hidden;
}
</style>
