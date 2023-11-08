<template>
  <div class="hero min-h-screen" :style="bgImg">
    <div v-if="img" class="hero-overlay bg-opacity-60"></div>
    <div
      class="hero-content"
      :class="{
        'text-neutral-content': img,
        'flex-col-reverse lg:flex-row-reverse': !center,
      }"
    >
      <slot name="side"></slot>
      <img
        v-if="!center && !!!this.$slots.side && figure"
        :src="figure"
        alt=""
        class="max-w-sm rounded-box shadow-2xl"
      />
      <div class="flex-1">
        <div v-if="title || desc" class="mx-auto max-w-xl">
          <h1
            v-if="title"
            class="text-3xl lg:text-5xl font-bold capitalize text-center"
            :class="{ 'mb-6': desc, 'lg:text-start': !center }"
            v-html="title"
          ></h1>
          <p
            v-if="desc"
            class="md:text-lg xl:text-2xl font-light text-center"
            :class="{
              'mb-6': !!this.$slots.default,
              'lg:text-start': !center,
              'opacity-60': !img,
            }"
            v-html="desc"
          ></p>
        </div>
        <slot></slot>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    title: {
      type: String,
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
