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
            <div
              class="flex items-center justify-center lg:justify-start gap-2 mb-6"
            >
              <img src="images/logo/jz-32.png" alt="" class="app-img" />
              <span href="#" class="font-bold text-xl normal-case"
                >Job<span class="text-primary">zone</span></span
              >
            </div>
            <h2
              class="mb-6 font-light text-2xl lg:text-4xl text-center lg:text-start"
            >
              Sign in to <br class="hidden lg:inline" />
              your account
            </h2>
            <form action="" class="grid grid-cols-1 gap-6">
              <label class="block">
                <span class="text-xs font-semibold opacity-60 capitalize"
                  >username</span
                >
                <input
                  type="text"
                  id="username"
                  placeholder="Enter your username"
                  class="app-input"
                />
              </label>
              <label class="block">
                <span class="text-xs font-semibold opacity-60 capitalize"
                  >password</span
                >
                <input
                  type="password"
                  id="password"
                  placeholder="Enter your password"
                  class="app-input"
                />
              </label>
              <button class="btn btn-block btn-primary">sign in</button>
            </form>
            <button class="btn btn-outline btn-primary">
              new to jobzone? join now
            </button>
          </template>
        </AppCard>
      </div>
    </template>
  </AppHero>
</template>
