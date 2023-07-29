return {
    "nvim-lualine/lualine.nvim",
    event = { "BufRead", "BufNewFile", "VimEnter" },
    opts = {
        options = {
            icons_enabled = true,
            theme = "auto",
            component_separators = "|",
            section_separators = { left = '', right = '' },
        },
        sections = {
            lualine_x = {},
            lualine_y = {
                'filetype', 'progress'
            },
            lualine_z = {
                { 'location', separator = { right = '' }, left_padding = 2 },
            },
        },
    },
}
