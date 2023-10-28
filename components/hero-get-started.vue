<template>
  <AppHero
    desc='Welcome to Jobzone, where your job search is safeguarded by cutting-edge machine learning, <br class="inline lg:hidden"/>ensuring a fraud-free experience.'
    :loose="true"
    img="images/pass-job-form-6000x4000.jpg"
    :center="false"
  >
    <template #side>
      <div
        class="animated fadeInUp flex-1 border border-base-content border-opacity-5 shadow-inner w-full lg:w-96"
      >
        <AppCard class="!max-w-none !max-h-none">
          <template #body>
            <AppComboMark class="justify-center lg:justify-start mb-6" />
            <h2
              class="mb-6 font-light text-2xl lg:text-4xl text-center lg:text-start"
            >
              Sign in <br class="hidden lg:inline" />
              to Jobzone
            </h2>
            <form action="" class="grid grid-cols-1 gap-6">
              <AppInput label="email" type="email" input-id="email" />
              <InputPassword />
              <button type="submit" class="btn btn-block btn-primary">
                sign in
              </button>
            </form>
            <button type="button" class="btn btn-outline btn-primary">
              new to jobzone? join now
            </button>
          </template>
        </AppCard>
      </div>
    </template>
  </AppHero>
</template>
