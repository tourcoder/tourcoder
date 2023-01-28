---
title: "以太坊开发笔记"
slug: yi-tai-fang-kai-fa
author: Bin Hua
lastmod: 2020-08-13T08:10:57Z
date: 2017-09-12T16:00:00Z
tags: ["eth", "以太坊"]
---

通过椭圆曲线算法生成钥匙对（公钥和私钥），以太坊采用的是secp256k1曲线。公钥采用uncompressed模式，生成的私钥为长度32的16进制字串，公钥为长度64的公钥字串。公钥04开头。
把公钥去掉04，剩下的进行keccak-256的哈希，得到长度64的16进制字串，丢掉前面24个，拿后40个，再加上"0x"，即为以太坊地址。
整个过程可以归纳为：

Get Private-key
Private-key -> Public-key
Public-key -> Address

#### 以太坊合约

```
pragma solidity ^0.4.26;
 contract Token{
    uint256 public totalSupply;
 
    function balanceOf(address _owner) public constant returns (uint256 balance);
    function transfer(address _to, uint256 _value) public returns (bool success);
    function transferFrom(address _from, address _to, uint256 _value) public returns   
    (bool success);
    function approve(address _spender, uint256 _value) public returns (bool success);
    function allowance(address _owner, address _spender) public constant returns 
    (uint256 remaining);
    event Transfer(address indexed _from, address indexed _to, uint256 _value);
    event Approval(address indexed _owner, address indexed _spender, uint256 
    _value);
}
contract DEMOToken is Token {
 
    string public name = "DEMO"; 
    uint8 public decimals = 2; 
    string public symbol = "DEMO"; 
 
    function DEMO(uint256 _initialAmount, string _tokenName, uint8 _decimalUnits, string _tokenSymbol) public {
        totalSupply = _initialAmount * 10 ** uint256(_decimalUnits);
        balances[msg.sender] = totalSupply; 
 
        name = _tokenName;                   
        decimals = _decimalUnits;          
        symbol = _tokenSymbol;
    }
 
    function transfer(address _to, uint256 _value) public returns (bool success) {
 
 
        require(balances[msg.sender] >= _value && balances[_to] + _value > balances[_to]);
        require(_to != 0x0);
        balances[msg.sender] -= _value;
        balances[_to] += _value;
        emit Transfer(msg.sender, _to, _value);
        return true;
    }
 
 
    function transferFrom(address _from, address _to, uint256 _value) public returns 
    (bool success) {
        require(balances[_from] >= _value && allowed[_from][msg.sender] >= _value);
        balances[_to] += _value;
        balances[_from] -= _value;
        allowed[_from][msg.sender] -= _value;
        emit Transfer(_from, _to, _value);
        return true;
    }
    function balanceOf(address _owner) public constant returns (uint256 balance) {
        return balances[_owner];
    }
 
 
    function approve(address _spender, uint256 _value) public returns (bool success)   
    { 
        require((_value == 0) || (allowed[msg.sender][_spender] == 0));
        allowed[msg.sender][_spender] = _value;
        emit Approval(msg.sender, _spender, _value);
        return true;
    }
 
    function allowance(address _owner, address _spender) public constant returns (uint256 remaining) {
        return allowed[_owner][_spender];
    }
    mapping (address => uint256) balances;
    mapping (address => mapping (address => uint256)) allowed;
}
```