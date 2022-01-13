<template>
    <div class="dao">
        <div class="act">
            <button class="btn btn-primary" @click="add()">+ 추가</button>
        </div>
        <ul>
            <li v-for="(data, index) in propsdata" v-bind:key="index">
                {{data.name}}
            </li>
        </ul>

        <ul>
            <li v-for="(data, index) in state.data" v-bind:key="index">
                {{data}}
            </li>
        </ul>
    </div>
</template>

<script>
import { reactive } from 'vue'

export default {
    props : ["propsdata"],
    setup(){
        const state = reactive({
            data:['메모1', '메모2', '메모3']
        })

        const add = ()=>{
            state.data.push("추가되었습니다")
        }

        return {state, add}
    }
    
};
</script>

<style>
.dao ul {
    list-style: none;
    padding: 0%;
    margin: 0%;
    border-top: solid #eee 1px;
}

.act {
    padding: 10px 10px 5px 5px;
    text-align: right;
}
</style> 