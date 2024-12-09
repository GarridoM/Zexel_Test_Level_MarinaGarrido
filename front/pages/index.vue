<template>
  <div class="container mt-5 pt-4">

    <h1 class="display-4 mt-2 mb-4">{{ $t('hi') }}</h1>

    <div class="app-description-container text-center mb-5">
      <h2 class="mb-3">{{ $t('app_description') }}</h2>
      <div class="divider"></div>
    </div>

    <div>
      <h2 class="h4 mb-3">{{ $t('main_functions') }}</h2>
      <div class="d-flex justify-content-between">
        <NuxtLink to="/payments" class="btn btn-corporate flex-fill m-2 p-2">
          <div class="h5">{{ $t('payments') }}</div>
        </NuxtLink>
        <NuxtLink to="/countries" class="btn btn-corporate flex-fill m-2 p-2">
          <div class="h5">{{ $t('countries') }}</div>
        </NuxtLink>
      </div>
    </div>

  </div>
</template>