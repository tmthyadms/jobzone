<template>
  <footer class="footer items-center p-10 border-t border-base-300">
    <aside class="items-center grid-flow-col">
      <IconHash :width="32" />
      <p>Copyright © 2023 - All right reserved by Timothy Adams J.</p>
    </aside>
    <nav
      class="grid-flow-col md:place-self-center justify-self-center md:justify-self-end"
    >
      <div v-for="social in socials" class="tooltip" :data-tip="social.tip">
        <a :href="social.url" class="btn btn-square btn-ghost">
          <component :is="social.component" :width="20" />
        </a>
      </div>
    </nav>
  </footer>
</template>

<script>
export default {
  data() {
    return {
      socials: [
        {
          url: 'https://www.linkedin.com/in/tmthyadms',
          tip: 'LinkedIn',
          component: 'IconLinkedin',
        },
        {
          url: 'https://github.com/tmthyadms',
          tip: 'GitHub',
          component: 'IconGithub',
        },
      ],
    };
  },
};
</script>

<style scoped>
[data-theme='autumn'] .bi-linkedin {
  @apply fill-[#0072b1];
}

[data-theme='autumn'] .bi-github {
  @apply fill-[#171515];
}
</style>
