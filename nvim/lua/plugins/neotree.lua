return {
    "nvim-neo-tree/neo-tree.nvim",
    branch = "v3.x",
    dependencies = {
        "nvim-lua/plenary.nvim",
        "nvim-tree/nvim-web-devicons", -- not strictly required, but recommended
        "MunifTanjim/nui.nvim",
    },
    cmd = "Neotree",
    keys = {
        { "<leader>t",  ":Neotree<cr>",        desc = "open neotree" },
        { "<leader>th", ":Neotree toggle<cr>", desc = "close neotree" },
    },
    window = {
        width = 10,
    },
}
