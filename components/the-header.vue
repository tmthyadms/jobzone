<template>
  <header
    class="sticky top-0 z-30 px-4 bg-base-100 bg-opacity-90 shadow-sm backdrop-blur"
  >
    <div class="navbar">
      <div class="flex-1">
        <AppComboMark :link="true" />
      </div>
      <div class="flex-none">
        <div id="tip-theme" class="tooltip tooltip-left" :data-tip="themeTip">
          <label
            role="button"
            class="btn btn-ghost btn-circle swap swap-rotate"
          >
            <input type="checkbox" v-model="theme.isDarkMode" />
            <IconMoon :width="20" class="swap-on" />
            <IconSun :width="20" class="swap-off" />
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
        storage: 'isDarkMode',
        isDarkMode: false,
      },
    };
  },
  watch: {
    'theme.isDarkMode'(newFlag) {
      this.setTheme(newFlag);
    },
  },
  computed: {
    themeTip() {
      return this.theme.isDarkMode ? this.theme.dark.tip : this.theme.light.tip;
    },
  },
  mounted() {
    const userPref = JSON.parse(localStorage.getItem(this.theme.storage));
    this.theme.isDarkMode = userPref ?? this.theme.isDarkMode;
    this.setTheme(this.theme.isDarkMode);
    this.shadowOnScroll();
  },
  methods: {
    setTheme(isDarkMode) {
      document.body.parentNode.dataset.theme = isDarkMode
        ? this.theme.dark.current
        : this.theme.light.current;
      localStorage.setItem(this.theme.storage, isDarkMode);
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
