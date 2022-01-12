<template>
    <div>
        <div v-for="(data, index) in propsdata" v-bind:key="index">
            <span><img src="{ data.mainImage }}"/></span>
            <br/>
            <span>NFT : {{ data.name }}</span>                
        </div>
    </div>
</template>

<script>
export default {
	props:["propsdata"]
};
</script>

<style>
.subject {
    color: blue;
    font-style: oblique;
    padding: 30px;
    text-align: center;
}
.userList {
    margin: 30px 0px 30px 0px;
}
</style>