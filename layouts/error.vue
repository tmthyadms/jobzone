<template>
  <AppHero
    title='404 - job not found <span class="loading loading-ball loading-md lg:loading-lg text-primary"></AppHero>'
    desc="Uh-oh! It seems this job is playing hide and seek. Head back to our homepage to uncover more job treasures."
    :main-max-w="false"
  >
    <div class="flex justify-center">
      <a href="/home" class="btn btn-primary mx-auto">take me home</a>
    </div>
  </AppHero>
</template>

<script>
export default {
  layout: 'pre-sign-in',
};
</script>
