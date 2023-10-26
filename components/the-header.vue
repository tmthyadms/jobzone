<template>
  <header
    class="sticky top-0 z-30 px-4 bg-base-100 bg-opacity-90 shadow-sm backdrop-blur"
  >
    <div class="navbar">
      <div class="flex-1">
        <a href="#" class="flex gap-2 items-center">
          <img src="images/logo/jz-32.png" alt="Jobzone Logo" class="app-img" />
          <span class="font-bold text-lg lg:text-xl normal-case"
            >Job<span class="text-primary">zone</span></span
          >
        </a>
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
            <div class="swap-on"><IconMoon :width="20" /></div>
            <div class="swap-off"><IconSun :width="20" /></div>
          </label>
        </div>
      </div>
    </div>
  </header>
</template>

<script>
export default {
  data() {
    return {
      theme: {
        light: {
          current: 'corporate',
          tip: 'Switch to dark mode',
        },
        dark: {
          current: 'business',
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
    this.shadowOnScroll();
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
    shadowOnScroll() {
      document.body.onscroll = () => {
        const header = document.querySelector('header');
        if (window.scrollY > 0) header.classList.add('shadow', 'ease-out');
        else header.classList.remove('shadow', 'ease-in');
      };
    },
  },
};
</script>
