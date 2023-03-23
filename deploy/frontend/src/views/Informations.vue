<script setup>

    import { storeToRefs } from 'pinia'
    import { useInformationsStore } from '../store/informations'

    const { informations, loading, error } = storeToRefs(useInformationsStore())

    const { fetchInformations } = useInformationsStore()

    fetchInformations()

</script>

<template>
    <main>
        <div v-if="loading">loading</div>

        <div v-if="error">{{  error.message }}</div>

        <div v-if="informations" class="index">
            <li 
                v-for="information in informations"
                :key="information.id"
            >   
                <h1>{{ information.title }}</h1>
                <p>{{ information.text }}</p>

            </li>
        </div>

    </main>
</template>