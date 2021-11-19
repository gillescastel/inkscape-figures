# VSCode-LaTeX-Inkscape
A way to integrate LaTeX, VSCode, and Inkscape in macOS

## Abstract

I use LaTeX heavily in past two years for both academic work and professional work, and I think I'm quite proficient in terms of type thing out in LaTeX. But when I see this blog post from **Gilles Castel**-[How I'm able to take notes in mathematics lectures using LaTeX and Vim](https://castel.dev/post/lecture-notes-1/) and also [How I draw figures for my mathematical lecture notes using Inkscape](https://castel.dev/post/lecture-notes-2/), I finally realize that I'm still too naive. 

I took quite a few math courses, hence after find out this incredible workflow, I decide to adapt the whole setup from Linux-Vim to macOS-VSCode. So, if you're interested in this and in the same situation as me, namely if you don't want to jump into Linux and Vim, follow me!

## Disclaimer

Please look through the two blog posts above from Gilles Castel! They are incredible, and worth spending your time to really understand how all things works, and what's the motivation behind all these. I'm only a copy-cat who want to mimic his workflow, but with a little patient to set up whole thing in my environment. Definitely show the respect to the original author!

## Setup For Typing Blasting Fast

First thing first, please set up your VSCode with LaTeX properly with [LaTeX Workshop](https://marketplace.visualstudio.com/items?itemName=James-Yu.latex-workshop), there are lots of tutorial online, just check them out and set them up properly.

Now, we go through thing one by one follow Gilles Castel's blog post.

### Tex Conceal

This is probably the only thing I don't like that much in Gilles Castel's set up. I'm quite comfortable looking at LaTeX source code for formula, and I don't think they look that nice. But if you want to set them up in VSCode, there are an extension [here](https://github.com/Pancaek/vsc-conceal), I personally have no experience with this particular setup, feel free to try them out though.

### Snippets

#### What’s a snippet?

A snip­pet is a short reusable piece of text that can be triggered by some other text. For example, when I type `dm` and press Tab, the word `dm` will be expanded to a math environment:

<p align="center">
	<img src="https://github.com/sleepymalc/sleepymalc/blob/main/Vscode-LaTEx-Inkscape/gif/dm.gif" width="500"/>
</p>

If you are a math guy, you may need to type some inline math like `$$`, which is kind of painful. But with snippet, you can have 

<p align="center">
	<img src="https://github.com/sleepymalc/sleepymalc/blob/main/Vscode-LaTEx-Inkscape/gif/inline.gif" width="500"/>
</p>

See? You just type `fm`, and then your snippet not only automatically type `$$`for you, it also sends your cursor between `$$`!

As you can imagine, this can be quite complex. For example, you can even have something like this:

<p align="center">
	<img src="https://github.com/sleepymalc/sleepymalc/blob/main/Vscode-LaTEx-Inkscape/gif/table2_5.gif" width="500"/>
</p>

or this:

<p align="center">
	<img src="https://github.com/sleepymalc/sleepymalc/blob/main/Vscode-LaTEx-Inkscape/gif/pmatrix.gif" width="500"/>
</p>

Too fast to keep track of? For the first snippet, I type `table2 5`, and then it generates a table with 2 rows and 5 columns. For the second one, I type `pmat` for matrix, and then type `2 4` to indicate that I want a 2 by 4 matrix, then boom! My snippets do that for me in an instant!

Feeling it? Let try to set up this step by step. And maybe you can create your own snippets also!

### HyperSnips for Math

If you look around in VSCode extension marketplace to find UltiSnips' equivalence, you probably will find [Vsnips](https://marketplace.visualstudio.com/items?itemName=corvofeng.Vsnips). But I'm not sure why this is the case, I can't figure out how to set up _ properly. Hence, I find another alternative, which is [HyperSnips](https://marketplace.visualstudio.com/items?itemName=draivin.hsnips). But hold on, don't download this too quickly! We will use [HyperSnips for Math](https://marketplace.visualstudio.com/items?itemName=OrangeX4.hsnips) instead, and I'll explain why in a moment. Before then, please first download [HyperSnips for Math](https://marketplace.visualstudio.com/items?itemName=OrangeX4.hsnips). Now, just follow the instruction, copy [latex.hsnips](https://github.com/sleepymalc/VSCode-LaTeX-Inkscape/blob/main/VSCode-setting/Snippets/latex.hsnips) into `$HOME/Library/Application Support/Code/User/hsnips/`, and you're good to go!

To modify this file, you can either go to this file in your finder or use VSCode built-in command function. For command function, 

1. Press `shift+cmd+space` to type in some command to VSCode.
2. Type `>HyperSnips: Open Snippet File`
3. Choose `latex.hsnips`

Now, let move on. Oh wait, I need to explain to you why I want to use [HyperSnips for Math](https://marketplace.visualstudio.com/items?itemName=OrangeX4.hsnips). This is because this version support *math mode*. Namely, you can specify a particular snippet will **only** be triggered in math environment. This is particularly useful when you need to switch beck and forth between text environment and math environment. When you use snippets after a while, you'll see why this is important!

For further and detailed explanation for snippets, please go to check out the original blog post! 

### Sympy and Mathematica

Unlike Gilles Castel's approach, there is an available extension out there for you to simplify your math calculation already! Please go to checkout [Latex SYMPY Calculator](https://marketplace.visualstudio.com/items?itemName=OrangeX4.latex-sympy-calculator). It's works like follows:

<p align="center">
	<img src="https://github.com/sleepymalc/sleepymalc/blob/main/Vscode-LaTEx-Inkscape/gif/integral.gif" width="500"/>
</p>

Magic right? Let's set it up! First, please look at the installation document provided by [Latex Sympy Calculator](https://marketplace.visualstudio.com/items?itemName=OrangeX4.latex-sympy-calculator). After your installation is done, you can then set up the keybinding for calculating the math expression. Personally, I use `shift+e`, where `e` stands for evaluate, to calculate in the way that it will append an equal sign and the answer right after your formula, just like above. And if you don't want to show the intermediate steps of your calculation, you can use `shift+r`, where `r` stands for replace, to directly replace the whole formula and give me the answer only. See the demo below:

<p align="center">
	<img src="https://github.com/sleepymalc/sleepymalc/blob/main/Vscode-LaTEx-Inkscape/gif/integral2.gif" width="500"/>
</p>

You can find my key-binding set up in this repo. But stay tune, there is more to come! Let's go to the last thing covered in Gilles Castel's post, correcting spelling mistakes.

### Correcting spelling mistakes on the fly

Although my typing speed is quite high, but I have typo all the times. So this is a must for me, actually. And surprisingly, this is the hardest thing until now for me to set it up right. Let's see how we can configure this functionality in VSCode!

#### multi-command

Firstly, you need to download [multi-command](https://marketplace.visualstudio.com/items?itemName=ryuta46.multi-command) to perform this. And this is a very powerful extension, which allow you to do a sequence of action in one shortcut. We will use this later on also, and that's the place it shines.

#### Code Spell Checker

And then, after searching for some times, I find out that there is a popular spelling checker out there which meets our needs, [Code Spell Checker](https://marketplace.visualstudio.com/items?itemName=streetsidesoftware.code-spell-checker). Just download it, it's useful.

#### LTeX(Not required)

If you are bad in grammar like me, you definitely want to install [LTeX](https://marketplace.visualstudio.com/items?itemName=valentjn.VSCode-ltex) to check some simple grammar mistakes for you. Although it's not powerful like [Grammarly](https://www.grammarly.com/), not even comparable, but it's still a good reference for you to keep your eyes on some simple mistakes you may overlook.

Now, it's time to configure all these. Open your Keyboard Shortcuts page in VSCode, which is in the bottom left

<p align="center">
	<img src="https://github.com/sleepymalc/sleepymalc/blob/main/Vscode-LaTEx-Inkscape/jpg/keyboard.png" alt="drawing" width="400"/>  
</p>

And then go into it's `JSON` file, which is at the upper right:

<p align="center">
	<img src="https://github.com/sleepymalc/sleepymalc/blob/main/Vscode-LaTEx-Inkscape/jpg/keyboard2.png" alt="drawing" width="200"/>
</p>

Now, paste the following code in `keybindings.json`:

```json
{
	"key": "cmd+l",
        "command": "extension.multiCommand.execute",
        "args": {
		"sequence": [
        	"cSpell.goToPreviousSpellingIssue",
	        {
                "command": "editor.action.codeAction",
        	    "args": {
	                "kind": "quickfix",
                    "apply": "first"
                }
            },
            "cursorUndo",
        ]
    }
},
```

Make sure that the curly braces above have a tailing comma, otherwise VSCode will complain about it.

Now, as long as you see there is a spelling error, you just type `cmd+l`, the keybinding will do the following things:

1. Use one of the default function from cSpell's: `goToPreviousSpellingIssue`, which jump your cursor on that spelling error word
2. Triggered a default editor action, with the argument being `quickfix` to open a quick fix drop down list, and choose the `first` suggestion
3. Move your cursor back by `cursorUndo`

Here is a quick demo for how it works when typing:

<p align="center">
	<img src="https://github.com/sleepymalc/sleepymalc/blob/main/Vscode-LaTEx-Inkscape/gif/spell.gif" width="500"/>
</p>

Additionally, if you also want to correct your grammar error, I use the shortcut `cmd+k` to trigger a quick-fix for a general error. The setting looks like this:
```json
{
    "key": "cmd+k",
    "command": "extension.multiCommand.execute",
    "args": {
        "sequence": [
            "editor.action.marker.prev",
            {
                "command": "editor.action.codeAction",
                "args": {
                    "kind": "quickfix",
                    "apply": "first"
                }
            },
            "cursorUndo",
        ]
    }
 },
```

Now, the first part is over. Let's go to the next truly beautiful, elegant and exciting world, drawing with [Inkscape](https://inkscape.org/zh-hant/).

## Drawing Like a Pro

Before we go to any setup detail, let's first look at some figures I draw right after I have set this up:

<p align="center">
	<img src="https://github.com/sleepymalc/sleepymalc/blob/main/Vscode-LaTEx-Inkscape/jpg/inkscape_example1.png" width="500"/>
</p>

<p align="center">
	<img src="https://github.com/sleepymalc/sleepymalc/blob/main/Vscode-LaTEx-Inkscape/jpg/inkscape_example2.png" width="500"/>
</p>

<p align="center">
	<img src="https://github.com/sleepymalc/sleepymalc/blob/main/Vscode-LaTEx-Inkscape/jpg/inkscape_example3.png" width="500"/>
</p>

This is quite eye-pleasing, right? Those are some drawing I made when taking Linear programming lectures. But this is just my naive drawing, compare to Gilles Castel's examples, this is nothing. Definitely check it out for the original blog. 

One last thing is that I'll assume you have already install [VSCode Vim](https://marketplace.visualstudio.com/items?itemName=vscodevim.vim). While this is not required, but if you don't want to use it, then you'll need to assign different keybinding. Anyway, you'll see what I mean until then!

### Inkscape

A big question is, why Inkscape? In Gilles Castel's blog, he had already explained it. One reason is that although TikZ can do the job for drawing vector figures in LaTeX with original support, it's too slow to set all diagram right. This is so true, since my experience with TikZ is *nice looking, intuitive* but also *slow, bulky*. For example, in one of my assignment for graph theory, I have to do graph partition by running a BFS(bread-first search). This is what's the source code looks like:

<p align="center">
	<img src="https://github.com/sleepymalc/sleepymalc/blob/main/Vscode-LaTEx-Inkscape/jpg/source-code.png" width="200"/>
</p>

You think this is it? No, this is not even half of them. And yes, I admit that the result is not bad, the initial graph looks like this:

<p align="center">
	<img src="https://github.com/sleepymalc/sleepymalc/blob/main/Vscode-LaTEx-Inkscape/jpg/tikz.png" width="500"/>
</p>

but to let VSCode to compile this, this is not fun at all. This large amount of nested environment, it takes *[latexindent](https://ctan.org/pkg/latexindent)* to auto-indent them for almost five seconds, and then compile them by *pdfLaTeX* takes about 5 more seconds. That's not efficient at all, especially when you want some instant feedback for some small changes. 

However, by using Inkscape, you only need to type(Ok, not quite, you don't need to type them out actually, you'll see) the following:

```latex
\begin{figure}[H]
	\centering
	\incfig{figure's name}
	\caption{Your caption}
	\label{fig:label}
\end{figure}
```

And then you're done! And also, the compilation time for this is shorter than you can ever expect. Let's get started then!

### Set up the Environment in LaTeX

First thing first, include the following in your header

```latex
\usepackage{import}
\usepackage{xifthen}
\usepackage{pdfpages}
\usepackage{transparent}

\newcommand{\incfig}[1]{%
    \def\svgwidth{\columnwidth}
    \import{./Figures/}{#1.pdf_tex}
}
```

This assumes that your LaTeX project's home directory looks like this:

```bash
LaTeX_project
    │
    ├── LaTex.tex
    │
    ├── LaTex.pdf
    │
    ├── Figures
    │    │
    │    ├── fig1
    │    ├── fig2
    │    .
    │	 .
    .
    .
```

Now, let's get into the fun part. Let's set up the short-cut for this.

### Inkscape

Apparently, you need to install [Inkscape](https://inkscape.org/zh-hant/) first. I recommend you to install this in terminal. I assume that you have your [`homebrew`](https://brew.sh/) installed. Then, just type the following into your terminal:

```bash
brew install --cask inkscape
```

### Inkscape figure manager

This is a figure manager developed by Gilles Castel, and here is the [repo](https://github.com/gillescastel/inkscape-figures). I recommend you to follow the installation instruction there. Here is just some guideline for you

1. You need to download [choose](https://github.com/chipsenkbeil/choose) first, for later usages.

2. Type this in your terminal
   ```bash
   pip3 install inkscape-figures
   ```

3. type `inkscape-figure` in your terminal to make sure you have corrected install it.

If you're using Linux and Vim, then you are done already. But since you're using macOS and VSCode, please follow me, there is some more thing for you to configure.

#### Modify

Firstly, please type the following command in your terminal

```bash
where inkscape-figures 
```
to find out where the `inkscape-figures` is installed. In my environment, I use Anaconda quite a lot, so mine is `/Users/pbb/opt/anaconda3/bin/inkscape-figures`. 

Now, go to a **relative directory**, in my case, it's in `/Users/pbb/opt/anaconda3/lib/python3.8/site-packages/inkscapefigures`. Open this directory by VSCode, there is something for you to modify.

Ok, I know you probably don't have that much patient now, so I have a modified version available [here](https://github.com/sleepymalc/VSCode-LaTeX-Inkscape/blob/main/Inkscape-setting/Inkscape-figure-manager/main.py). If you don't want to know the detail, you can just copy this `main.py` and replace the current one. If you're interesting, lets me explain it for you.

##### Detail Explanation

In Gilles Castel's approach, he uses the shortcut `ctrl-f` to trigger this script, which will copy the whole line's content depending on cursor's position, and the script will send the snippets by the function

```python
def latex_template(name, title):
    return '\n'.join((r"\begin{figure}[ht]",
                      r"    This is a custom LaTeX template!",
                      r"    \centering",
                      rf"    \incfig[1]{{{name}}}",
                      rf"    \caption{{{title}}}",
                      rf"    \label{{fig:{name}}}",
                      r"\end{figure}"))
```
to `stdout`, and then create a figure by the `name`, which is the content of the line.

But this in VSCode is impossible, hence we don't need this, we'll use another approach, namely we'll accomplish the task by command line. And if we leave this function as it was, then it will literally send all these snippets into our terminal, which is quite annoying. So the modified version just remove this snippet completely.

Ok, the detailed explanation is over, let's move on.

### Command Runner

The last thing you need to install is [Command Runner](https://marketplace.visualstudio.com/items?itemName=edonet.vscode-command-runner). This will allow you to send command into terminal with shortcut. The configuration is in [`setting.json`](https://github.com/sleepymalc/VSCode-LaTeX-Inkscape/blob/main/VSCode-setting/settings.json). Please copy the content into your own `setting.json`. Then, the only thing left is with that missing snippet part. Before we set it up, we look at the demonstration.

### Demo

<p align="center">
	<img src="https://github.com/sleepymalc/sleepymalc/blob/main/Vscode-LaTEx-Inkscape/gif/demo-inkscape.gif" width="900"/>
</p>


Don't know what happen? Let me break it down for you. Firstly, I change into `insert` mode in VSCode Vim and type my new figure's name `figure-test`. And then, I press `ctrl+f` to trigger a keybinding. Then it will automatically create an Inkscape figure named `figure-test` for me and open it. 

Feel exciting? Let's set it up!

### Set up Inkscape figure manager

The only thing you need to do is to copy the [keybindings.json](https://github.com/sleepymalc/VSCode-LaTeX-Inkscape/blob/main/VSCode-setting/keybindings.json) and [settings.json](https://github.com/sleepymalc/VSCode-LaTeX-Inkscape/blob/main/VSCode-setting/settings.json) into your own `keybindings.json` and `settings.json` and then you're done. But let me explain it to you, in case that you want to modify it to meet your need later on.

### Explanation

There are three different command in Inkscape figure manager. We break it down one by one.

#### 1. Watch

Since Inkscape in default does not save the file in `pdf+latex`, hence we need Inkscape figure manager to help us. We need to first open the a file watcher to *watch* the file for any changes. If there is any, then file watcher will tell Inkscape to save the file in `pdf+latex` format.

To open the file watcher, you can type `inkscape-figures watch` in the terminal. In my case, I set up a shortly for this. In [keybindings.json](https://github.com/sleepymalc/VSCode-LaTeX-Inkscape/blob/main/VSCode-setting/keybindings.json), we have 

```json
{
    "key": "ctrl+f",
    "command": "command-runner.run",
    "args": {
        "command": "inkscapeStart",
        "terminal": {
            "name": "runCommand",
            "shellArgs": [],
            "autoClear": true,
            "autoFocus": false
        }
    },
    "when": "editorTextFocus && vim.active && vim.use<C-f> && !inDebugRepl && vim.mode == 'Visual'"
}
```

for starting the Inkscape figure manager. And the command is defined in [settings.json](https://github.com/sleepymalc/VSCode-LaTeX-Inkscape/blob/main/VSCode-setting/settings.json):

```json
"command-runner.commands": {
    "inkscapeStart": "inkscape-figures watch"
}
```

In detailed, we just use `command runner` to run the command we defined in [settings.json](https://github.com/sleepymalc/VSCode-LaTeX-Inkscape/blob/main/VSCode-setting/settings.json), in this case, I explicitly tell the keybinding `ctrl+f` will trigger `inkscapeStart` when I'm in `Visual` mode in Vim, which is just `inkscape-figures watcher` as defined above.

Notice that we set the `autoFocus=false` for the terminal `command runner` use since we don't want a pop-up terminal to distract us. If you want to see whether the command is triggered correctly every time, you can set it to `true`.

#### 2. Create

Same as above, we also use `ctrl+f` to trigger `inkscape-figures create` command. But in this case, we do a little bit more than that. We set up our [keybindings.json](https://github.com/sleepymalc/VSCode-LaTeX-Inkscape/blob/main/VSCode-setting/keybindings.json) as 

```json
{
	"key": "ctrl+f",
	"command": "extension.multiCommand.execute",
	"args": {
		"sequence": [
			"editor.action.clipboardCopyAction",
			"editor.action.insertLineAfter",
			"cursorUp",
			"editor.action.deleteLines",
			{
			"command": "editor.action.insertSnippet",
			"args": {
				"name": "incfig"
				}
			},
			{
				"command": "command-runner.run",
				"args": {
					"command": "inkscapeCreate",
				},
				"terminal": {
					"name": "runCommand",
					"shellArgs": [],
					"autoClear": true,
					"autoFocus": false
				}
			},
		]
	},
	"when": "editorTextFocus && vim.active && vim.use<C-f> && !inDebugRepl && vim.mode == 'Insert'"
},
```

and also in [settings.json](https://github.com/sleepymalc/VSCode-LaTeX-Inkscape/blob/main/VSCode-setting/settings.json):

```json
"command-runner.commands": {
    "inkscapeCreate": "inkscape-figures create ${selectedText} ${workspaceFolder}/Figures/"
}
```

We break it down what `ctrl+f` do in `Insert` mode exactly step by step. We see that when we press `ctrl+f` in `Insert` mode, we trigger `multiCommand.execute` to execute a sequence of instructions, which are

1. Copy the content into your clipboard of the line your cursor at
2. We insert a bland line after since we need to insert snippet, and that's will delete a additional line. You can try to delete this and the next instruction, and see what happens.
3. After insert a new line, we move back our cursor.
4. We delete that copied content by removing this line.
5. We insert an snippet defined in [`latex.json`](https://github.com/sleepymalc/VSCode-LaTeX-Inkscape/blob/main/VSCode-setting/Snippets/latex.json). **Notice that this is the defualt snippet functionality built-in VSCode, not what we have use above**. I'll explain where to copy this file in a minute.
6. Lastly, we send a command in terminal by `command runner`, with the command `inkscapeCreate` we defined in [settings.json](https://github.com/sleepymalc/VSCode-LaTeX-Inkscape/blob/main/VSCode-setting/settings.json). Then we're done!

In the fifth instruction, we need to use the snippet like 

```json
{
	"incfig": {
		"prefix": "incfig",
		"body": [
			"\\begin{figure}[H]",
			"\t\\centering",
			"\t\\incfig{${1:$CLIPBOARD}}",
			"\t\\caption{${2:title}}",
			"\t\\label{fig:${1:$CLIPBOARD}}",
			"\\end{figure}",
		],
		"description": "Inserts mathematical diagram"
	}
}
```

which is just the snippet we remove from Inkscape figure manager's source code! It's back again, in a different approach! You can paste this into your configuration by the following steps:

1. Press `shift+cmd+p` to open the VSCode command 
2. Type `snippets`, and choose `Preferences: Configure User Snippets`. 
3. Choose `New Global Snippets file...`
4. Enter `latex` to create a new file.
5. Paste the above snippets in to that file.

Now, let's see the last thing I have to share with you.

#### 3. Edit

Again, we also use `ctrl+f` to trigger `inkscape-figures edit` command. We set up our [keybindings.json](https://github.com/sleepymalc/VSCode-LaTeX-Inkscape/blob/main/VSCode-setting/keybindings.json) as 

```json
{
	"key": "ctrl+f",
	"command": "command-runner.run",
	"args": {
		"command": "inkscapeEdit",
		"terminal": {
			"name": "runCommand",
			"shellArgs": [],
			"autoClear": true,
			"autoFocus": false
		}
	},
	"when": "editorTextFocus && vim.active && vim.use<C-f> && !inDebugRepl && vim.mode == 'Normal'"
},
```

and also in [settings.json](https://github.com/sleepymalc/VSCode-LaTeX-Inkscape/blob/main/VSCode-setting/settings.json):

```json
"command-runner.commands": {
    "inkscapeEdit": "inkscape-figures edit ${workspaceFolder}/Figures/"
}
```

This is what's you should expect when you want to edit a particular figure:
<p align="center">
	<img src="https://github.com/sleepymalc/sleepymalc/blob/main/Vscode-LaTEx-Inkscape/gif/demo-edit-inkscape.gif" width="900"/>
</p>

This is where [choose](https://github.com/chipsenkbeil/choose) comes into play. When you press `ctrl+f` in `Normal` mode, you'll trigger the `inkscape-figures edit` command, and it'll look into your `Figures/` subfolder to see what figures you have and pop out a window for you to choose. After you press `enter`, it will open that file for you to edit. In my demo, I create another figure named `figure-test2`, and then modify it a little, and compile it again.

Notice that there is one more thing for you to modify in the source code in `main.py` in inkscape figure manager. Since Gilles Castel originally use `figures/` as his subfolder name to store figures, so you need to change every `figures/` in the source code into `Figures/` if you're modifying the source-code by your own rather than copy mine.

### Overall Workflow to Create a New Figure in VSCode with Inkscape

This is the whole set up I have, and let's wrap this up, since I know this may be quite overwhelming.

1. Before you start your project, please go to `Visual` mode by entering `v` in `Normal` mode. And then press `ctrl+f`. This will set up the file watcher.
2. When you want to create a new figure, go into a new line, type the name of your figure in `Insert` mode, then press `ctrl+f`. This will create a new figure with the name you typed, and open it in Inkscape for you.
3. When you have done drawing your figure, as long as you press `cmd+s`, it will automatically save the figure in `pdf+latex` for you, then you can close Inkscape.
4. When you want to edit one of your figure, you press `ctrl+f` in `Normal` mode, it will pop out a window for you to choose the figure you want to edit. And the rest is the same as 3. 

## Credits

Again, thanks to Gilles Castel, this workflow really fit my style. Although it originally works in Linux+Vim only, but the idea is the most important thing. Without his wonder post, I can't even imagine this is possible. But now it is! Definitely go to his original post to show him some love.

## TODO

If you read through Gilles Castel's posts, you'll find out that I don't have any solution for [inkscape-shortcut-manager](https://github.com/gillescastel/inkscape-shortcut-manager), this is because it depends on a particular library called `Xlib`, which is only for Linux. 

Currently, there is a repo called [python-xlib](https://github.com/python-xlib/python-xlib) for macOS, but it's still underdeveloped. And although they claim that the most functionality is done, but there is still some bug when I want to use [inkscape-shortcut-manager](https://github.com/gillescastel/inkscape-shortcut-manager). Hence, let's see what can we do for this part. I currently just use the default shortcut, and this works quite well for me. If there is any alternative, definitely let me know!

### Updates(9.27.21)

After some reseraching, although there is a way to let the original script in [inkscape-shortcut-manager](https://github.com/gillescastel/inkscape-shortcut-manager) running correctly, but since it depends on `xlib`, which is no longer used by macOS for almost every application(including inkscape, as expected), hence the only thing I can do now is to give up. In a perceivable future, if I have time to find an alternative way to interrupt the window activity in macOS, I'll try to configure it for macOS.

## Related Project
1. [Academic_Template](https://github.com/sleepymalc/Academic_Template)(A general LaTeX template for making PPT by beamer and Academic Report)
2. [gillescastel/inkscape-figures](https://github.com/gillescastel/inkscape-figures)
3. [gillescastel/inkscape-shortcut-manager](https://github.com/gillescastel/inkscape-shortcut-manager)
4. [chipsenkbeil/choose](https://github.com/chipsenkbeil/choose)
