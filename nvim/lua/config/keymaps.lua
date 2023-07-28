vim.g.mapleader = " "

-- Go back to explorer
vim.keymap.set("n", "<leader><BS>", vim.cmd.Ex)

-- VsCode like keymaps
vim.keymap.set("n", "<C-s>", ":w<cr>")
vim.keymap.set("i", "<C-s>", "<esc>:w<cr>")
vim.keymap.set("n", "<C-q>", ":wq<cr>")
vim.keymap.set("n", "<C-Q>", ":q!<cr>")

-- Move lines
vim.keymap.set("v", "J", ":m '>+1<CR>gv=gv")
vim.keymap.set("v", "K", ":m '<-2<CR>gv=gv")

-- Move page up/down keeping cursor on the middle
vim.keymap.set("n", "<C-d>", "<C-d>zz")
vim.keymap.set("n", "<C-u>", "<C-u>zz")

-- Search keeps cursor on the middle
vim.keymap.set("n", "n", "nzzzv")
vim.keymap.set("n", "N", "Nzzzv")

-- On paste keeps selection pasted and not replace with the replaced text
vim.keymap.set("x", "<leader>p", "\"_dP")

-- Yank to clipboard
vim.keymap.set("n", "<leader>y", "\"+y")
vim.keymap.set("n", "<leader>Y", "\"+Y")
vim.keymap.set("v", "<leader>y", "\"+y")
vim.keymap.set("v", "<leader>Y", "\"+Y")
vim.keymap.set("n", "<leader>p", "\"+p")
vim.keymap.set("n", "<leader>P", "\"+P")
vim.keymap.set("v", "<leader>p", "\"+p")
vim.keymap.set("v", "<leader>P", "\"+P")

-- Delete to black hole register
vim.keymap.set("n", "<leader>d", "\"_d")
vim.keymap.set("v", "<leader>d", "\"_d")

-- Regex search improvements
vim.keymap.set("n", "<leader>s", [[:%s/\<<C-r><C-w>\>/<C-r><C-w>/gI<Left><Left><Left>]])

-- Make file executable
vim.keymap.set("n", "<leader>x", "<cmd>!chmod +x %<CR>", { silent = true })
