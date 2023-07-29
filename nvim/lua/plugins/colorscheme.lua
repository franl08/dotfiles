return {
    "folke/tokyonight.nvim",
    name = "tokyonight",
    lazy = false,
    priority = 1000,
    opts = {},
    config = function()
        require("tokyonight").setup({
            no_bold = true
        })
        vim.cmd.colorscheme("tokyonight-night")
        --vim.api.nvim_set_hl(0, "Normal", { bg = "none" })
        --vim.api.nvim_set_hl(0, "NormalFloat", { bg = "none" })
    end,
}
