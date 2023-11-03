<template>
  <AppHero
    desc='Welcome to Jobzone, where your job search is safeguarded by cutting-edge machine learning, <br class="inline lg:hidden"/>ensuring a fraud-free experience.'
    img="images/pass-job-form-6000x4000.jpg"
    :center="false"
  >
    <template #side>
      <div class="animated fadeInUp flex-1 w-full lg:w-96">
        <CardSignIn />
      </div>
    </template>
  </AppHero>
</template>
