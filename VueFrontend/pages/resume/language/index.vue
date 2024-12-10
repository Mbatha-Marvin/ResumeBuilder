<template>
  <PartialsHeader title="Language Section">
    <PartialsSpinner :items="languages">
      <div class="row">
        <p class="d-inline">
          Language List
          <NuxtLink :to="'/resume/language/create'" class="btn btn-sm btn-success float-end">
            <i class="bi bi-plus-square"></i>{{ " " }}Create
          </NuxtLink>
        </p>
      </div>
      <div v-for="(language, index) in languages" :key="index" class="card mt-2">
        <div class="card-content collapse show">
          <div class="card-body card-dashboard">
            <div class="row">
              <p class="float-start">
                <strong>{{ index + 1 }}</strong>
              </p>
            </div>

            <form @submit.prevent="submitLanguageForm(index)" class="form form-horizontal needs-validation" novalidate>
              <div class="form-body">
                <div class="row">
                  <div class="col-md-4">
                    <div class="form-group mb-2">
                      <label class="label-control" for="card_title">Card Title</label>
                      <select v-model="language.card_title" class="form-select border-primary" required>
                        <option selected :value="language.card_title">
                          {{ language.card_title }}
                        </option>
                        <option>Language</option>
                        <option>Spoken Language</option>
                      </select>
                      <span class="invalid-feedback">Please Select Card Title</span>
                    </div>
                  </div>

                  <div class="col-md-4">
                    <div class="form-group mb-2">
                      <label class="label-control" for="language_name">Language Name</label>
                      <input v-model="language.language_name" type="text" id="language_name"
                        class="form-control border-primary" placeholder="Language Name" required />
                      <span class="invalid-feedback">Language Name is required</span>
                    </div>
                  </div>

                  <div class="col-md-4">
                    <div class="form-group mb-2">
                      <label class="label-control" for="profeciency_level">Proficiency Level</label>
                      <input v-model="language.profeciency_level" type="text" id="profeciency_level"
                        class="form-control border-primary" placeholder="Proficiency Level" required />
                      <span class="invalid-feedback">Proficiency Level is required</span>
                    </div>
                  </div>
                </div>
                <ActionButtons :loadingStates="loadingStates" :index="index" :onUpdate="() => submitLanguageForm(index)"
                  :onDelete="deleteLanguage" />
              </div>
            </form>
          </div>
        </div>
      </div>
    </PartialsSpinner>
  </PartialsHeader>
</template>

<script setup>
import { ref, onMounted } from "vue";
import ActionButtons from "~/components/Partials/ActionButtons.vue";
const languages = ref([]);
const loadingStates = ref([]);
const { $showToast, $axios } = useNuxtApp();
const { get, loading, response, error } = useNuxtApp().$useAxios;
const user_id = 1;

definePageMeta({
  layout: "sidestar",
});

useHead({
  title: "Languages",
  meta: [
    { name: "description", content: "View Languages" },
    { property: "og:title", content: "Languages" },
    { property: "og:description", content: "View Languages." },
  ],
});

const getLanguage = async () => {
  loadingStates.value = [true];
  await get(`/user/${user_id}/language/`);
  if (response) {
    languages.value = response.value.data;
    loadingStates.value = [loading.value];
  } else {
    console.error("Error fetching languages:", error.value);
    loadingStates.value = [loading.value];
  }
};

const updateLanguage = async (languageIndex) => {
  loadingStates.value[languageIndex] = { updating: true };
  const languageToUpdate = languages.value[languageIndex];
  try {
    await $axios.patch(
      `/user/${languageToUpdate.user_id}/language/${languageToUpdate.language_id}`,
      languageToUpdate
    );
    $showToast("Language updated!");
  } catch (error) {
    console.error("Error updating:", error);
  } finally {
    loadingStates.value[languageIndex] = { updating: false };
  }
};

const deleteLanguage = async (language_id, languageIndex) => {
  loadingStates.value[languageIndex] = { deleting: true };
  try {
    const response = await $axios.delete(`/user/${user_id}/language/${language_id}`);
    if (response.status === 200) {
      $showToast("Language deleted!");
      await getLanguage();
    }
  } catch (error) {
    console.error("Error deleting language:", error);
  } finally {
    loadingStates.value[languageIndex] = { deleting: false };
  }
};

const submitLanguageForm = async (languageIndex) => {
  const form = document.querySelector(".needs-validation");

  if (!form.checkValidity()) {
    form.classList.add("was-validated");
    return;
  }

  await updateLanguage(languageIndex);
};

onMounted(() => {
  getLanguage();
});
</script>

<style></style>
