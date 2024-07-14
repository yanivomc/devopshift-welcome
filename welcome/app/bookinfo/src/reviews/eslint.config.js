import { FlatCompat } from "@eslint/eslintrc";

const compat = new FlatCompat();

export default compat.config({
    extends: "eslint:recommended",
    env: {
        node: true,
        es6: true
    },
    rules: {
        "no-console": "off",
        "no-unused-vars": "off",
        "no-undef": "off",
        "no-empty": "off",
        "no-extra-semi": "off"
    }
});
