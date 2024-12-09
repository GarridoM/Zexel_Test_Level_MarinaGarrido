<template>
  <div class="container-fluid">
    <div class="row">
      <div class="alert alert-danger fixed-top py-1 text-center d-flex align-items-center justify-content-center"
        style="height: 50px;">
        <p class="mb-0 small">{{ $t('app_disclaimer') }}</p>
      </div>
      <div class="col-12">
        <slot />
      </div>
    </div>
  </div>
</template>
