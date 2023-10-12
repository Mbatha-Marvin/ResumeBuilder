<template>
    <div class="row py-4 px-2">
            <div class="col-md-12">
                <div class="card mb-2">
                    <div class="card-body rounded">
                        <h4 class="text-center text-uppercase bold">Profile Section</h4>
                    </div>
                </div>
                <div class="card mb-2">
                    <div class="card-content collapse show">
                        <div class="card-body card-dashboard">
                            <div class="row">
                                <p class="d-inline">Profile List
                                    <NuxtLink :to="'/resume/profile/create'" class="btn btn-sm btn-success float-end"><i
                                            class="bi bi-plus-square"></i>{{ ' ' }}Create
                                    </NuxtLink>
                                </p>
                            </div>
                            <div v-for="(profile, index) in profiles" :key="index" class="card mt-2">
                                <div class="card-content collapse show">
                                    <div class="card-body card-dashboard">

                                        <div class="row">
                                            <p class="float-start"><strong>{{ index + 1 }}</strong></p>
                                        </div>

                                        <form @submit.prevent="submitProfile(index)"
                                            class="form form-horizontal needs-validation" novalidate>
                                            <div class="form-body">
                                                <div class="row">
                                                    <div class="col-md-6">
                                                        <div class="form-group row mb-2">
                                                            <label class="col-md-3 label-control" for="first_name">First
                                                                Name</label>
                                                            <div class="col-md-9">
                                                                <input v-model="profile.first_name" type="text"
                                                                    id="first_name" class="form-control border-primary"
                                                                    placeholder="First Name" name="first_name" required>
                                                                <span class="invalid-feedback">First Name is
                                                                    required</span>
                                                            </div>
                                                        </div>
                                                    </div>
                                                    <div class="col-md-6">
                                                        <div class="form-group row mb-2">
                                                            <label class="col-md-3 label-control" for="last_name">Last
                                                                Name</label>
                                                            <div class="col-md-9">
                                                                <input v-model="profile.last_name" type="text"
                                                                    id="last_name" class="form-control border-primary"
                                                                    placeholder="Last Name" name="last_name" required>
                                                                <span class="invalid-feedback">Last Name is
                                                                    required</span>
                                                            </div>
                                                        </div>
                                                    </div>
                                                </div>
                                                <div class="row">
                                                    <div class="col-md-6">
                                                        <div class="form-group row mb-2">
                                                            <label class="col-md-3 label-control" for="middle_name">Middle
                                                                Name</label>
                                                            <div class="col-md-9">
                                                                <input v-model="profile.middle_name" type="text"
                                                                    id="middle_name" class="form-control border-primary"
                                                                    placeholder="Middle Name" name="middle_name" required>
                                                                <span class="invalid-feedback">Middle Name is
                                                                    required</span>
                                                            </div>
                                                        </div>
                                                    </div>
                                                    <div class="col-md-6">
                                                        <div class="form-group row mb-2">
                                                            <label class="col-md-3 label-control" for="image_url">Image url
                                                                link</label>
                                                            <div class="col-md-9">
                                                                <input v-model="profile.image_url" type="text"
                                                                    id="image_url" class="form-control border-primary"
                                                                    placeholder="Image url link" name="image_url" required>
                                                                <span class="invalid-feedback">Image url link is
                                                                    required</span>
                                                            </div>
                                                        </div>
                                                    </div>
                                                </div>

                                                <div class="row">
                                                    <div class="col-md-6">
                                                        <div class="form-group row mb-2">
                                                            <label class="col-md-3 label-control"
                                                                for="linkedin_url">linkedIn Url</label>
                                                            <div class="col-md-9">
                                                                <input v-model="profile.linkedin_url" type="text"
                                                                    id="linkedin_url" class="form-control border-primary"
                                                                    placeholder="linkedIn Url" name="linkedin_url" required>
                                                                <span class="invalid-feedback">linkedIn Url is
                                                                    required</span>
                                                            </div>
                                                        </div>
                                                    </div>
                                                    <div class="col-md-6">
                                                        <div class="form-group row mb-2">
                                                            <label class="col-md-3 label-control" for="github_url">Github
                                                                url link</label>
                                                            <div class="col-md-9">
                                                                <input v-model="profile.github_url" type="text"
                                                                    id="github_url" class="form-control border-primary"
                                                                    placeholder="Github url link" name="github_url"
                                                                    required>
                                                                <span class="invalid-feedback">Github url link is
                                                                    required</span>
                                                            </div>
                                                        </div>
                                                    </div>
                                                </div>

                                                <div class="row">
                                                    <div class="col-md-6">
                                                        <div class="form-group row mb-2">
                                                            <label class="col-md-3 label-control" for="address">Postal
                                                                Address</label>
                                                            <div class="col-md-9">
                                                                <input v-model="profile.address" type="text" id="address"
                                                                    class="form-control border-primary"
                                                                    placeholder="Postal Address" name="address" required>
                                                                <span class="invalid-feedback">Postal Address is
                                                                    required</span>
                                                            </div>
                                                        </div>
                                                    </div>
                                                    <div class="col-md-6">
                                                        <div class="form-group row mb-2">
                                                            <label class="col-md-3 label-control"
                                                                for="personal_website">Personal Website Url</label>
                                                            <div class="col-md-9">
                                                                <input v-model="profile.personal_website" type="text"
                                                                    id="personal_website"
                                                                    class="form-control border-primary"
                                                                    placeholder="Personal Website Url"
                                                                    name="personal_website" required>
                                                                <span class="invalid-feedback">Personal Website Url is
                                                                    required</span>
                                                            </div>
                                                        </div>
                                                    </div>
                                                </div>

                                                <div class="row">
                                                    <div class="col-md-6">
                                                        <div class="form-group row mb-2">
                                                            <label class="col-md-3 label-control" for="city">City
                                                                Name</label>
                                                            <div class="col-md-9">
                                                                <input v-model="profile.city" type="text" id="city"
                                                                    class="form-control border-primary"
                                                                    placeholder="City Name" name="city" required>
                                                                <span class="invalid-feedback">City Name is
                                                                    required</span>
                                                            </div>
                                                        </div>
                                                    </div>
                                                    <div class="col-md-6">
                                                        <div class="form-group row mb-2">
                                                            <label class="col-md-3 label-control" for="country">Country of
                                                                Residence</label>
                                                            <div class="col-md-9">
                                                                <input v-model="profile.country" type="text" id="country"
                                                                    class="form-control border-primary"
                                                                    placeholder="Country of Residence" name="country"
                                                                    required>
                                                                <span class="invalid-feedback">Country of Residence is
                                                                    required</span>
                                                            </div>
                                                        </div>
                                                    </div>
                                                </div>

                                                <div class="row">
                                                    <div class="col-md-6">
                                                        <div class="form-group row mb-2">
                                                            <label class="col-md-3 label-control" for="user_work_title">Job
                                                                Title</label>
                                                            <div class="col-md-9">
                                                                <input v-model="profile.user_work_title" type="text"
                                                                    id="user_work_title" class="form-control border-primary"
                                                                    placeholder="Job Title" name="user_work_title" required>
                                                                <span class="invalid-feedback">Job Title is
                                                                    required</span>
                                                            </div>
                                                        </div>
                                                    </div>
                                                    <div class="col-md-6">
                                                        <div class="form-group row mb-2">
                                                            <label class="col-md-3 label-control" for="user_summary">Job
                                                                summary</label>
                                                            <div class="col-md-9">
                                                                <input v-model="profile.user_summary" type="text"
                                                                    id="user_summary" class="form-control border-primary"
                                                                    placeholder="Job summary" name="user_summary" required>
                                                                <span class="invalid-feedback">Job summary is
                                                                    required</span>
                                                            </div>
                                                        </div>
                                                    </div>
                                                </div>

                                                <div class="row">
                                                    <div class="col-md-6">
                                                        <div class="form-group row mb-2">
                                                            <label class="col-md-3 label-control" for="objectives">Job
                                                                Objective</label>
                                                            <div class="col-md-9">
                                                                <input v-model="profile.objectives" type="text"
                                                                    id="objectives" class="form-control border-primary"
                                                                    placeholder="Job Objective" name="objectives" required>
                                                                <span class="invalid-feedback">Job Objective is
                                                                    required</span>
                                                            </div>
                                                        </div>
                                                    </div>
                                                </div>

                                                <div class="row">
                                                    <div class="col-md-6">
                                                        <div class="form-group row mb-2">
                                                            <label class="col-md-3 label-control"
                                                                for="location">Skills:</label>
                                                            <div class="col-md-9">
                                                                <div class="input-group">
                                                                    <input v-model="newSkill" type="text"
                                                                        class="form-control border-primary"
                                                                        placeholder="Type and click (+) to add to list" />
                                                                    <span class="input-group-text"><button
                                                                            class="btn btn-sm btn-success" type="button"
                                                                            @click="addSkill(index)"><i
                                                                                class="bi bi-plus"></i></button></span>
                                                                </div>
                                                            </div>
                                                        </div>
                                                    </div>

                                                    <div class="col-md-6">
                                                        <div class="card mb-2">
                                                            <div class="card-content collapse show">
                                                                <div class="card-body card-dashboard">
                                                                    <div class="row">
                                                                        <p>Skills here</p>
                                                                        <hr
                                                                            class="border border-primary border-2 opacity-50">
                                                                    </div>

                                                                    <ol type="1">
                                                                        <li v-for="(skill, skillIndex) in profile.skills"
                                                                            :key="skillIndex" class="my-2 mx-2">{{
                                                                                skill }} <button type="button"
                                                                                class="btn btn-sm btn-danger"
                                                                                @click="removeSkill(index, skillIndex)"><i
                                                                                    class="bi bi-x"></i></button></li>
                                                                    </ol>

                                                                </div>
                                                            </div>
                                                        </div>
                                                    </div>
                                                </div>

                                                <div class="row">
                                                    <div class="col-md-6">
                                                        <div class="form-group row mb-2">
                                                            <label class="col-md-3 label-control"
                                                                for="location">Hobbies:</label>
                                                            <div class="col-md-9">
                                                                <div class="input-group">
                                                                    <input v-model="newHobby" type="text"
                                                                        class="form-control border-primary"
                                                                        placeholder="Type and click (+) to add to list" />
                                                                    <span class="input-group-text"><button
                                                                            class="btn btn-sm btn-success" type="button"
                                                                            @click="addHobby(index)"><i
                                                                                class="bi bi-plus"></i></button></span>
                                                                </div>
                                                            </div>
                                                        </div>
                                                    </div>

                                                    <div class="col-md-6">
                                                        <div class="card mb-2">
                                                            <div class="card-content collapse show">
                                                                <div class="card-body card-dashboard">
                                                                    <div class="row">
                                                                        <p>Hobbies here</p>
                                                                        <hr
                                                                            class="border border-primary border-2 opacity-50">
                                                                    </div>

                                                                    <ol type="1">
                                                                        <li v-for="(hobby, hobbyIndex) in profile.hobbies"
                                                                            :key="hobbyIndex" class="my-2 mx-2">{{
                                                                                hobby }} <button type="button"
                                                                                class="btn btn-sm btn-danger"
                                                                                @click="removeHobby(index, hobbyIndex)"><i
                                                                                    class="bi bi-x"></i></button></li>
                                                                    </ol>

                                                                </div>
                                                            </div>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>

                                            <div class="row">
                                                <div class="form-actions my-2">
                                                    <button type="submit" class="btn btn-sm btn-primary mx-2 float-start">
                                                        <i class="bi bi-pencil-square"></i>{{ ' ' }}Update
                                                    </button>

                                                    <button @click="deleteProfile(profile.profile_id)"
                                                        class="btn btn-sm btn-danger float-end mx-2"><i
                                                            class="bi bi-trash3"></i>
                                                        {{ ' ' }}Delete
                                                    </button>
                                                </div>
                                            </div>

                                        </form>

                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
</template>
  
<script>
import { defineComponent, ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';

definePageMeta({
    layout: "sidestar",
});

export default defineComponent({
    name: 'profileList',
    setup() {

        const profiles = ref([]);
        const axios = useNuxtApp().$axios;
        const user_id = 1;
        const router = useRouter();
        const newSkill = ref('');
        const newHobby = ref('');

        //Adding a new skill
        const addSkill = (profileIndex) => {
            if (newSkill.value.trim() !== '') {
                const profileSkillToAdd = profiles.value[profileIndex];
                if (profileSkillToAdd.skills.length < 5) {
                    profileSkillToAdd.skills.push(newSkill.value);
                }
                else {
                    console.log('Errow while adding, exceeded 5');
                }
                newSkill.value = '';
            }
        };
        const removeSkill = (profileIndex, skillIndex) => {
            const profileSkillToRemove = profiles.value[profileIndex];
            profileSkillToRemove.skills.splice(skillIndex, 1);
        };

        //Adding a new hobby
        const addHobby = (profileIndex) => {
            if (newHobby.value.trim() !== '') {
                const profileHobbyToAdd = profiles.value[profileIndex];
                if (profileHobbyToAdd.hobbies.length < 5) {
                    profileHobbyToAdd.hobbies.push(newHobby.value);
                }
                else {
                    console.log('Errow while adding, exceeded 5');
                }
                newHobby.value = '';
            }
        };
        const removeHobby = (profileIndex, hobbyIndex) => {
            const profileHobbyToRemove = profiles.value[profileIndex];
            profileHobbyToRemove.hobbies.splice(hobbyIndex, 1);
        };

        const getProfiles = async () => {
            try {
                const response = await axios.get(`/user/${user_id}/profile/`);
                profiles.value = response.data;
            } catch (error) {
                console.error('Error fetching profiles:', error);
            }
        };

        const updateProfile = async (profileIndex) => {
            try {
                await axios.patch(
                    `/user/${profileIndex.user_id}/profile/${profileIndex.profile_id}`,
                    profileIndex
                ).then(function (response) {
                    console.log(response);
                    router.push('/resume/profile');
                });
            } catch (error) {
                console.error('Error updating:', error);
            }
        };

        const deleteProfile = async (profile_id) => {
            try {
                await axios.delete(`/user/${user_id}/profile/${profile_id}`);
                getProfiles();
            } catch (error) {
                console.error('Error deleting profile:', error);
            }
        };

        const submitProfile = async (profileIndex) => {
            const profileToUpdate = profiles.value[profileIndex];
            const form = document.querySelector('.needs-validation');

            if (!form.checkValidity()) {
                form.classList.add('was-validated');
                return;
            }

            updateProfile(profileToUpdate);
        };


        onMounted(() => {
            getProfiles();
        });

        return {
            profiles,
            deleteProfile,
            submitProfile,
            addSkill,
            newSkill,
            removeSkill,
            addHobby,
            newHobby,
            removeHobby,
        };
    },
});
</script>
  
<style></style>
  