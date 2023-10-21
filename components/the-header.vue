<template>
  <div
    class="sticky top-0 z-30 px-4 bg-base-100 bg-opacity-90 shadow-sm backdrop-blur"
  >
    <div class="navbar">
      <div class="flex-1">
        <a href="#" class="font-bold text-xl normal-case"
          >daisy<span class="text-primary">UI</span></a
        >
      </div>
      <div class="flex-none">
        <div
          id="tip-theme"
          class="tooltip tooltip-left"
          :data-tip="theme.light.tip"
        >
          <label
            role="button"
            class="btn btn-ghost btn-circle swap swap-rotate"
          >
            <input type="checkbox" v-model="theme.isDarkMode" />
            <div class="swap-on"><IconMoonStars :width="20" /></div>
            <div class="swap-off"><IconEmojiSunglasses :width="20" /></div>
          </label>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      theme: {
        light: {
          current: 'autumn',
          tip: 'Switch to dark mode',
        },
        dark: {
          current: 'coffee',
          tip: 'Switch to light mode',
        },
        isDarkMode: false,
      },
    };
  },
  watch: {
    'theme.isDarkMode'(newFlag) {
      this.setTheme(newFlag);
    },
  },
  mounted() {
    const userPref = JSON.parse(localStorage.getItem('isDarkMode'));
    this.theme.isDarkMode = userPref ?? this.theme.isDarkMode;
    this.setTheme(this.theme.isDarkMode);
  },
  methods: {
    setTheme(isDarkMode) {
      document.body.parentNode.dataset.theme = isDarkMode
        ? this.theme.dark.current
        : this.theme.light.current;
      document.getElementById('tip-theme').dataset.tip = isDarkMode
        ? this.theme.dark.tip
        : this.theme.light.tip;
      localStorage.setItem('isDarkMode', isDarkMode);
    },
  },
};
</script>
