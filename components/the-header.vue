<template>
  <header
    class="sticky top-0 z-30 px-4 bg-base-100 bg-opacity-90 shadow-sm backdrop-blur"
  >
    <div class="navbar">
      <div class="flex-1">
        <AppComboMark :link="true" />
      </div>
      <div class="flex-none gap-2">
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
        <div class="dropdown dropdown-bottom dropdown-end">
          <label
            tabindex="0"
            class="btn btn-primary btn-circle avatar online placholder"
          >
            <div class="rounded-full">jz</div>
          </label>
          <ul
            tabindex="0"
            class="dropdown-content menu p-2 shadow bg-base-100 rounded-box w-52"
          >
            <li><a>Profile</a></li>
            <li><button type="button" @click="signOut">Sign Out</button></li>
          </ul>
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
    'theme.isDarkMode'(newValue) {
      this.setTheme(newValue);
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
    signOut() {
      // TODO: clear common.id from profile store
      window.scrollTo({ top: 0, behavior: 'auto' });
      this.$router.push('/');
    },
  },
};
</script>
