%% Code Example
% Made by: AhmedSalih3d
% Github : https://github.com/AhmedSalih3d/Blend2Mesh

% Remember to download "readNPY" and "readNPYheader", from 
% https://github.com/kwikteam/npy-matlab to ensure this functionality
% works. Remember to check licenses.

%% Code with all functions inside
% Remember to save "BlenderIniplot" function in a different file, with the
% other two functions embedded if you want this to be a "commandline" tool.

%elems - connection between nodes in elements
%nodes - vertex position for each node 1 to N
[elems,nodes] = BlenderIniplot("Suzanne");

function [elems,nodes] = BlenderIniplot(filename)
    elems = readNPY(filename+"Elems.npy")+1;
    nodes = readNPY(filename+"Nodes.npy");
    A = vertexmatrix(elems,nodes);
    f = facematrix(elems);
    figure('name',filename,'NumberTitle','off');
    centerfig;
    hold off
    axis equal
    patch('faces',f, 'vertices',  A,'facecolor','c')
end


function f = facematrix(elems)
    range = (1:numel(elems)-sum(sum(isnan(elems))));
    f = elems';
    f(~isnan(f)) = range;
    f = f';
end

function A = vertexmatrix(elems,nodes)
    M = elems';
    A = nodes(M(~isnan(M)),:);
end
